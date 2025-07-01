function (frameTime) {

        if (!this._standardGamepadAvailable) {
            return;
        }

        this._scanPressedGamepadButtons();
        this._scanInclinedGamepadAxes();

        // Update target depending on user input.

        var target = this.target;

        var position = this.target.position;
        var xAxis = target.localTransform.x.normalize();
        var zAxis = target.localTransform.z.normalize();

        var moveSpeed = this.moveSpeed * frameTime / 20;

        if (this._moveForward) {
            // Opposite direction of z.
            position.scaleAndAdd(zAxis, -moveSpeed);
        }
        if (this._moveBackward) {
            position.scaleAndAdd(zAxis, moveSpeed);
        }
        if (this._moveLeft) {
            position.scaleAndAdd(xAxis, -moveSpeed);
        }
        if (this._moveRight) {
            position.scaleAndAdd(xAxis, moveSpeed);
        }

        target.rotateAround(target.position, this.up, -this._offsetPitch * frameTime * Math.PI / 360);
        var xAxis = target.localTransform.x;
        target.rotateAround(target.position, xAxis, -this._offsetRoll * frameTime * Math.PI / 360);

        /*
         * If necessary: trigger `update` event.
         * XXX This can economize rendering OPs.
         */
        if (this._moveForward === true || this._moveBackward === true || this._moveLeft === true
            || this._moveRight === true || this._offsetPitch !== 0 || this._offsetRoll !== 0)
        {
            this.trigger('update');
        }

        // Reset values to avoid lost of control.

        this._moveForward = this._moveBackward = this._moveLeft = this._moveRight = false;
        this._offsetPitch = this._offsetRoll = 0;

    }