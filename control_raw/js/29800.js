function PluginRegistry(serviceRegistry, configuration) {
        configuration = configuration || {};
        var _storage = configuration.storage || localStorage;
        if (!_storage.getItem) {
            _storage = _asStorage(_storage);
        }
        var _defaultTimeout = parseInt(_storage.getItem("pluginregistry.default.timeout"), 10) || undefined;
        var _state = "installed";
        var _parent;
        var _plugins = [];
        var _channels = [];
        var _pluginEventTarget = new EventTarget();
        var _installing = {};

        var internalRegistry = {
            serviceRegistry: serviceRegistry,
            registerService: serviceRegistry.registerService.bind(serviceRegistry),
            connect: function(url, handler, parent, timeout) {
                var channel = {
                    handler: handler,
                    url: url
                };

                function log(state) {
                    if (localStorage.pluginLogging) console.log(state + "(" + (Date.now() - channel._startTime) + "ms)=" + url); //$NON-NLS-1$ //$NON-NLS-0$
                }

                function sendTimeout(message) {
                    log("timeout"); //$NON-NLS-0$
                    var error = new Error(message);
                    error.name = "timeout";
                    handler({
                        method: "timeout",
                        error: error
                    });
                }
                
                timeout = timeout || _defaultTimeout;
                
                channel._updateTimeout = function() {
                    var message, newTimeout;
                    if (!this._connected && !this._closed) {
                        if (this._handshake) {
                            // For each plugin being loaded add 1000 ms extra time to the handshake timeout
                            var extraTimeout = 0;
                            _channels.forEach(function(c) {
                                if (!c._connected && !c._closed) {
                                    extraTimeout += 1000;
                                }
                            });
                            message = "Plugin handshake timeout for: " + url;
                           newTimeout = this._loading ? 5000 : (timeout || 60000) + extraTimeout;
                        } else {
                            message = "Plugin load timeout for: " + url;
                            newTimeout = timeout || 15000;
                        }
                    }
                    if (this._loadTimeout) clearTimeout(this._loadTimeout);
                    this._loadTimeout = 0;
                    if (newTimeout) this._loadTimeout = setTimeout(sendTimeout.bind(null, message), newTimeout);
                };

                var isWorker = !!(url.match(workerRegex) && typeof(Worker) !== "undefined");
                var isSharedWorker = !!(url.match(sharedWorkerRegex) && typeof(SharedWorker) !== "undefined");
                if ((!localStorage.useSharedWorkers || !isSharedWorker) && url.match(sharedWorkerRegex)) {
                    url = url.replace(sharedWorkerRegex, workerJS);
                    isSharedWorker = false;
                }
                if ((!localStorage.useWorkers || !isWorker) && url.match(workerRegex)) {
                    url = url.replace(workerRegex, pluginHtml);
                    isWorker = isSharedWorker = false;
                }               

                channel.url = url;
                channel._updateTimeout();
                channel._startTime = Date.now();
                if (isWorker) {
                    var worker;
                    if (isSharedWorker) {
                        worker = new SharedWorker(url);
                        channel.target = worker.port;
                        worker.port.start();
                        channel._close = function() {
                            worker.port.close();
                        };
                    } else {
                        worker = new Worker(url);
                        channel.target = worker;
                        channel._close = function() {
                            worker.terminate();
                        };
                    }
                    channel.postMessage = function(message) {
                        this.target.postMessage((this.useStructuredClone ? message : JSON.stringify(message)), []);
                    };
                    channel.target.addEventListener("message", function(evt) {
                    	_channelHandler(channel, evt);
                    });
                } else {
                   	var iframe = document.createElement("iframe"); //$NON-NLS-0$
                    iframe.name = url + "_" + channel._startTime;
					iframe.src = urlModifier(url);
                    iframe.onload = function() {
                        log("handshake"); //$NON-NLS-0$
                        channel._handshake = true;
                        channel._updateTimeout();
                    };
                    iframe.sandbox = "allow-scripts allow-same-origin allow-forms allow-popups"; //$NON-NLS-0$
                    iframe.style.width = iframe.style.height = "100%"; //$NON-NLS-0$
                    iframe.frameBorder = 0;
                    iframe.title = (parent || _parent).title;
                    (parent || _parent).appendChild(iframe);
                    channel.target = iframe.contentWindow;
                    channel.postMessage = function(message) {
                        this.target.postMessage((this.useStructuredClone ? message : JSON.stringify(message)), this.url);
                    };
                    channel._close = function() {
                        if (iframe) {
                            var frameParent = iframe.parentNode;
                            if (frameParent) {
                                frameParent.removeChild(iframe);
                            }
                            iframe = null;
                        }
                    }; 
                }
                channel.connected = function() {
                    log("connected"); //$NON-NLS-0$
                    this._connected = true;
                    this._updateTimeout();
                    
                };
                channel.loading = function() {
                    log("loading"); //$NON-NLS-0$
                    this._loading = true;
                    this._updateTimeout();
                };
                channel.close = function() {
                    log("closed"); //$NON-NLS-0$
                    this._closed = true;
                    this._updateTimeout();
                    this._close();
                };
                _channels.push(channel);
                return channel;
            },
            disconnect: function(channel) {
                for (var i = 0; i < _channels.length; i++) {
                    if (channel === _channels[i]) {
                        _channels.splice(i, 1);
                        try {
                            channel.close();
                        } catch (e) {
                            // best effort
                        }
                        break;
                    }
                }
            },
            removePlugin: function(plugin) {
                for (var i = 0; i < _plugins.length; i++) {
                    if (plugin === _plugins[i]) {
                        _plugins.splice(i, 1);
                        break;
                    }
                }
                _storage.removeItem("plugin." + plugin.getLocation());
            },
            getPersisted: function(url) {
            	var key = "plugin." + url;
            	var manifest = _storage.getItem(key);
            	if (manifest) {
            		manifest = JSON.parse(manifest);
            		if (manifest.created) {
            			return manifest;
            		}
            	}
            	return null;
            },
            persist: function(url, manifest) {
            	if (!manifest || !manifest.services || !manifest.services.length) {
            		_storage.removeItem("plugin." + url);
            		return;
            	}
                _storage.setItem("plugin." + url, JSON.stringify(manifest)); //$NON-NLS-0$
            },
            postMessage: function(message, channel) {
                channel.postMessage(message);
            },
            dispatchEvent: function(event) {
                try {
                    _pluginEventTarget.dispatchEvent(event);
                } catch (e) {
                    if (console) {
                        console.log("PluginRegistry.dispatchEvent " + e);
                    }
                }
            },
            loadManifest: function(url) {
                var d = new Deferred();
                var channel = internalRegistry.connect(url, function(message) {
                    if (!channel || !message.method) {
                        return;
                    }
                    if ("manifest" === message.method || "plugin" === message.method) { //$NON-NLS-0$
                        var manifest = message.params[0];
                        internalRegistry.disconnect(channel);
                        channel = null;
                        d.resolve(manifest);
                    } else if ("timeout" === message.method || "error" === message.method) {
                        internalRegistry.disconnect(channel);
                        channel = null;
                        d.reject(message.error);
                    } else if ("loading" === message.method) {
                        channel.loading();
                    }
                });
                return d.promise;
            },
            getState: function() {
                return _state;
            },
            handleServiceError: function(plugin, error) {
                if (error && (error.status === 401 || error.status === 491)) {
                    var headers = plugin.getHeaders();
                    var name = plugin.getName() || plugin.getLocation();
                    var span = document.createElement("span");
                    span.appendChild(document.createTextNode("Authentication required for: " + name + "."));
                    if (headers.login) {
                        span.appendChild(document.createTextNode(" "));
                        var anchor = document.createElement("a");
                        anchor.target = "_blank";
                        anchor.textContent = "Login";
                        anchor.href = headers.login;
                        if (!httpOrHttps.test(anchor.href)) {
                            console.log("Illegal Login URL: " + headers.login);
                        } else {
                            span.appendChild(anchor);
                            span.appendChild(document.createTextNode(" and re-try the request."));
                        }
                    }
                    var serializer = new XMLSerializer();
                    return {
                        Severity: "Error",
                        HTML: true,
                        Message: serializer.serializeToString(span)
                    };
                }
                if (error.__isError) {
                    var original = error;
                    error = new Error(original.message);
                    Object.keys(original).forEach(function(key) {
                        error[key] = original[key];
                    });
                    delete error.__isError;
                }
                return error;
            }
        };

        this.getLocation = function() {
            return "System";
        };

        this.getHeaders = function() {
            return {};
        };

        this.getName = function() {
            return "System";
        };

        this.getVersion = function() {
            return "0.0.0";
        };

        this.getLastModified = function() {
            return 0;
        };

        this.getState = internalRegistry.getState;

		function _channelHandler(channel, event) {
			try {
                var message;
                if (typeof channel.useStructuredClone === "undefined") {
                    var useStructuredClone = typeof event.data !== "string"; //$NON-NLS-0$
                    message = useStructuredClone ? event.data : JSON.parse(event.data);
                    channel.useStructuredClone = useStructuredClone;
                } else {
                    message = channel.useStructuredClone ? event.data : JSON.parse(event.data);
                }
                channel.handler(message);
            } catch (e) {
                // not a valid message -- ignore it
            }
		}

        function _messageHandler(event) {
            var source = event.source;
            _channels.some(function(channel) {
                if (source === channel.target) {
                    _channelHandler(channel, event);
                    return true; // e.g. break
                }
            });
        }


        this.init = function() {
            if (_state === "starting" || _state === "active" || _state === "stopping") {
                return;
            }
            addEventListener("message", _messageHandler, false);
            
            if (configuration.parent) {
                _parent = configuration.parent;
            } else {
                _parent = document.createElement("div"); //$NON-NLS-0$
                if (!configuration.visible) {
                    _parent.style.display = "none"; //$NON-NLS-0$
                    _parent.style.visibility = "hidden"; //$NON-NLS-0$
                }
                document.body.appendChild(_parent);
            }

            if (configuration.plugins) {
                Object.keys(configuration.plugins).forEach(function(key) {
		            var url = _normalizeURL(key);
		            //                    if (!httpOrHttps.test(url)) {
		            //                        console.log("Illegal Plugin URL: " + url);
		            //                        return;
		            //                    }
		            var plugin = this.getPlugin(url);
		            if (!plugin) {
		                var manifest = configuration.plugins[key];
		                if (typeof manifest !== "object") {
		                	manifest = internalRegistry.getPersisted(url) || {};
		                }
		                manifest.autostart = manifest.autostart || configuration.defaultAutostart || "lazy";
		                plugin = new Plugin(url, manifest, internalRegistry);
		                plugin._default = true;
		                _plugins.push(plugin);
		            } else {
		                plugin._default = true;
		            }
                }.bind(this));
            }
            _plugins.sort(function(a, b) {
                return a._getCreated() < b._getCreated() ? -1 : 1;
            });
            _state = "starting";
        };

        /**
         * Starts the plugin registry.
         * @name orion.pluginregistry.PluginRegistry#start
         * @return {orion.Promise} A promise that will resolve when the registry has been fully started.
         * @function 
         */
        this.start = function() {
            if (_state !== "starting") {
                this.init();
            }
            if (_state !== "starting") {
                return new Deferred().reject("Cannot start framework. Framework is already " + _state + ".");
            }
            var deferreds = [];
            _plugins.forEach(function(plugin) {
                var autostart = plugin._getAutostart();
                if ("started" === autostart || "active" === autostart) {
                    deferreds.push(plugin.start({
                        "transient": true
                    }));
                } else if ("lazy" === autostart) {
                    deferreds.push(plugin.start({
                        "lazy": true,
                            "transient": true
                    }));
                } else {
                    plugin._resolve();
                }
            });
            return Deferred.all(deferreds, function(e) {
                console.log("PluginRegistry.stop " + e);
            }).then(function() {
                _state = "active";
            });
        };

        /**
         * Shuts down the plugin registry.
         * @name orion.pluginregistry.PluginRegistry#stop
         * @function 
         * @returns {orion.Promise} A promise that will resolve when the registry has been stopped.
         */
        this.stop = function() {
            if (_state !== "starting" && _state !== "active") {
                return new Deferred().reject("Cannot stop registry. Registry is already " + _state + ".");
            }
            _state = "stopping";
            var deferreds = [];
            _plugins.forEach(function(plugin) {
                deferreds.push(plugin.stop({
                    "transient": true
                }));
            });
            return Deferred.all(deferreds, function(e) {
                console.log("PluginRegistry.stop " + e);
            }).then(function() {
                if (!configuration.parent) {
                    var parentNode = _parent.parentNode;
                    if (parentNode) {
                        parentNode.removeChild(_parent);
                    }
                }
                _parent = null;
                removeEventListener("message", _messageHandler);
                _state = "resolved";
            });
        };

        this.update = function() {
            this.stop().then(this.start.bind(this));
        };

        this.uninstall = function() {
            return new Deferred().reject("Cannot uninstall registry");
        };


        /**
         * Installs the plugin at the given location into the plugin registry.
         * @name orion.pluginregistry.PluginRegistry#installPlugin
         * @param {String} url The location of the plugin.
         * @param {Object} [optManifest] The plugin metadata.
         * @returns {orion.Promise} A promise that will resolve when the plugin has been installed.
         * @function 
         */
        this.installPlugin = function(url, optManifest) {
            url = _normalizeURL(url);
            //            if (!httpOrHttps.test(url)) {
            //                return new Deferred().reject("Illegal Plugin URL: " + url);
            //            }
            var plugin = this.getPlugin(url);
            if (plugin) {
                return new Deferred().resolve(plugin);
            }

            if (_installing[url]) {
                return _installing[url];
            }
            
            if (optManifest) {
            	if (optManifest.autostart === "lazy") {
	                optManifest = _mixin({}, internalRegistry.getPersisted(url), optManifest);
            	}
                plugin = new Plugin(url, optManifest, internalRegistry);
                _plugins.push(plugin);
                plugin._persist();
                internalRegistry.dispatchEvent(new PluginEvent("installed", plugin));
                return new Deferred().resolve(plugin);
            }

            var promise = internalRegistry.loadManifest(url).then(function(manifest) {
                plugin = new Plugin(url, manifest, internalRegistry);
                _plugins.push(plugin);
                plugin._persist();
                delete _installing[url];
                internalRegistry.dispatchEvent(new PluginEvent("installed", plugin));
                return plugin;
            }, function(error) {
                delete _installing[url];
                throw error;
            });
            _installing[url] = promise;
            return promise;
        };

        /**
         * Returns all installed plugins.
         * @name orion.pluginregistry.PluginRegistry#getPlugins
         * @return {orion.pluginregistry.Plugin[]} An array of all installed plugins.
         * @function 
         */
        this.getPlugins = function() {
            return _plugins.slice();
        };

        /**
         * Returns the installed plugin with the given URL.
         * @name orion.pluginregistry.PluginRegistry#getPlugin
         * @return {orion.pluginregistry.Plugin} The installed plugin matching the given URL, or <code>null</code>
         * if no such plugin is installed.
         * @function 
         */
        this.getPlugin = function(url) {
            var result = null;
            url = _normalizeURL(url);
            _plugins.some(function(plugin) {
                if (url === plugin.getLocation()) {
                    result = plugin;
                    return true;
                }
            });
            return result;
        };

        this.addEventListener = _pluginEventTarget.addEventListener.bind(_pluginEventTarget);

        this.removeEventListener = _pluginEventTarget.removeEventListener.bind(_pluginEventTarget);

        this.resolvePlugins = function() {
            var allResolved = true;
            _plugins.forEach(function(plugin) {
                allResolved = allResolved && plugin._resolve();
            });
            return allResolved;
        };
    }