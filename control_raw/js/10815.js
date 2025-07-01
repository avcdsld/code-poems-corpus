function(spec) {
            var button = this._createUploadButton({
                accept: spec.validation.acceptFiles,
                allowedExtensions: spec.validation.allowedExtensions,
                element: spec.element,
                folders: spec.folders,
                multiple: spec.multiple,
                title: spec.fileInputTitle
            });

            this._extraButtonSpecs[button.getButtonId()] = spec;
        }