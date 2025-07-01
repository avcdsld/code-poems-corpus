function VideoTexture(name, urlsOrVideo, scene, generateMipMaps, invertY, samplingMode) {
            if (generateMipMaps === void 0) { generateMipMaps = false; }
            if (invertY === void 0) { invertY = false; }
            if (samplingMode === void 0) { samplingMode = BABYLON.Texture.TRILINEAR_SAMPLINGMODE; }
            var _this = _super.call(this, null, scene, !generateMipMaps, invertY) || this;
            _this._autoLaunch = true;
            var urls;
            _this.name = name;
            if (urlsOrVideo instanceof HTMLVideoElement) {
                _this.video = urlsOrVideo;
            }
            else {
                urls = urlsOrVideo;
                _this.video = document.createElement("video");
                _this.video.autoplay = false;
                _this.video.loop = true;
            }
            _this._generateMipMaps = generateMipMaps;
            _this._samplingMode = samplingMode;
            if (!_this.getScene().getEngine().needPOTTextures || (BABYLON.Tools.IsExponentOfTwo(_this.video.videoWidth) && BABYLON.Tools.IsExponentOfTwo(_this.video.videoHeight))) {
                _this.wrapU = BABYLON.Texture.WRAP_ADDRESSMODE;
                _this.wrapV = BABYLON.Texture.WRAP_ADDRESSMODE;
            }
            else {
                _this.wrapU = BABYLON.Texture.CLAMP_ADDRESSMODE;
                _this.wrapV = BABYLON.Texture.CLAMP_ADDRESSMODE;
                _this._generateMipMaps = false;
            }
            if (urls) {
                _this.video.addEventListener("canplay", function () {
                    _this._createTexture();
                });
                urls.forEach(function (url) {
                    var source = document.createElement("source");
                    source.src = url;
                    _this.video.appendChild(source);
                });
            }
            else {
                _this._createTexture();
            }
            _this._lastUpdate = BABYLON.Tools.Now;
            return _this;
        }