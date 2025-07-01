function(ctx, status, message, details) {
				var node = ctx.node,
					tree = ctx.tree;

				function _clearStatusNode() {
					// Remove dedicated dummy node, if any
					var firstChild = node.children ? node.children[0] : null;
					if (firstChild && firstChild.isStatusNode()) {
						try {
							// I've seen exceptions here with loadKeyPath...
							if (node.ul) {
								node.ul.removeChild(firstChild.li);
								firstChild.li = null; // avoid leaks (DT issue 215)
							}
						} catch (e) {}
						if (node.children.length === 1) {
							node.children = [];
						} else {
							node.children.shift();
						}
					}
				}
				function _setStatusNode(data, type) {
					// Create/modify the dedicated dummy node for 'loading...' or
					// 'error!' status. (only called for direct child of the invisible
					// system root)
					var firstChild = node.children ? node.children[0] : null;
					if (firstChild && firstChild.isStatusNode()) {
						$.extend(firstChild, data);
						firstChild.statusNodeType = type;
						tree._callHook("nodeRenderTitle", firstChild);
					} else {
						node._setChildren([data]);
						node.children[0].statusNodeType = type;
						tree.render();
					}
					return node.children[0];
				}

				switch (status) {
					case "ok":
						_clearStatusNode();
						node._isLoading = false;
						node._error = null;
						node.renderStatus();
						break;
					case "loading":
						if (!node.parent) {
							_setStatusNode(
								{
									title:
										tree.options.strings.loading +
										(message ? " (" + message + ")" : ""),
									// icon: true,  // needed for 'loding' icon
									checkbox: false,
									tooltip: details,
								},
								status
							);
						}
						node._isLoading = true;
						node._error = null;
						node.renderStatus();
						break;
					case "error":
						_setStatusNode(
							{
								title:
									tree.options.strings.loadError +
									(message ? " (" + message + ")" : ""),
								// icon: false,
								checkbox: false,
								tooltip: details,
							},
							status
						);
						node._isLoading = false;
						node._error = { message: message, details: details };
						node.renderStatus();
						break;
					case "nodata":
						_setStatusNode(
							{
								title: message || tree.options.strings.noData,
								// icon: false,
								checkbox: false,
								tooltip: details,
							},
							status
						);
						node._isLoading = false;
						node._error = null;
						node.renderStatus();
						break;
					default:
						$.error("invalid node status " + status);
				}
			}