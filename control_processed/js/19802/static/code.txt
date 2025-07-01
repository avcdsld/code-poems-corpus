function () {
                return this._attachedCamera.inertialAlphaOffset !== 0 ||
                    this._attachedCamera.inertialBetaOffset !== 0 ||
                    this._attachedCamera.inertialRadiusOffset !== 0 ||
                    this._attachedCamera.inertialPanningX !== 0 ||
                    this._attachedCamera.inertialPanningY !== 0 ||
                    this._isPointerDown;
            }