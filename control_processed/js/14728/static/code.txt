function () {
        var gamepads = navigator.getGamepads();
        var e = {};

        // Trigger button bindings
        Object.keys(bindings).forEach(function (index) {
            var gamepad = gamepads[index];
            if (!gamepad) {
                return;
            }

            var mapping = null;
            if (gamepad.mapping !== "standard") {
                mapping = remap.get(gamepad.id);
            }

            var binding = bindings[index];

            // Iterate all buttons that have active bindings
            Object.keys(binding.buttons).forEach(function (button) {
                var last = binding.buttons[button];
                var mapped_button = button;
                var mapped_axis = -1;

                // Remap buttons if necessary
                if (mapping) {
                    mapped_button = mapping.buttons[button];
                    mapped_axis = mapping.analog[button];
                    if (mapped_button < 0 && mapped_axis < 0) {
                        // Button is not mapped
                        return;
                    }
                }

                // Get mapped button
                var current = gamepad.buttons[mapped_button] || {};

                // Remap an axis to an analog button
                if (mapping) {
                    if (mapped_axis >= 0) {
                        var value = mapping.normalize_fn(gamepad.axes[mapped_axis], -1, +button);

                        // Create a new object, because GamepadButton is read-only
                        current = {
                            "value" : value,
                            "pressed" : current.pressed || (Math.abs(value) >= deadzone)
                        };
                    }
                }

                me.event.publish(me.event.GAMEPAD_UPDATE, [ index, "buttons", +button, current ]);

                // Edge detection
                if (!last.pressed && current.pressed) {
                    api._keydown(e, last.keyCode, mapped_button + 256);
                }
                else if (last.pressed && !current.pressed) {
                    api._keyup(e, last.keyCode, mapped_button + 256);
                }

                // Update last button state
                last.value = current.value;
                last.pressed = current.pressed;
            });

            // Iterate all axes that have active bindings
            Object.keys(binding.axes).forEach(function (axis) {
                var last = binding.axes[axis];
                var mapped_axis = axis;

                // Remap buttons if necessary
                if (mapping) {
                    mapped_axis = mapping.axes[axis];
                    if (mapped_axis < 0) {
                        // axe is not mapped
                        return;
                    }
                }

                // retrieve the current value and normalize if necessary
                var value = gamepad.axes[mapped_axis];
                if (typeof(value) === "undefined") {
                    return;
                }
                if (mapping) {
                    value = mapping.normalize_fn(value, +axis, -1);
                }
                // normalize value into a [-1, 1] range value (treat 0 as positive)
                var range = Math.sign(value) || 1;
                if (last[range].keyCode === 0) {
                    return;
                }
                var pressed = (Math.abs(value) >= (deadzone + Math.abs(last[range].threshold)));

                me.event.publish(me.event.GAMEPAD_UPDATE, [ index, "axes", +axis, value ]);

                // Edge detection
                if (!last[range].pressed && pressed) {
                    // Release the opposite direction, if necessary
                    if (last[-range].pressed) {
                        api._keyup(e, last[-range].keyCode, mapped_axis + 256);
                        last[-range].value = 0;
                        last[-range].pressed = false;
                    }

                    api._keydown(e, last[range].keyCode, mapped_axis + 256);
                }
                else if ((last[range].pressed || last[-range].pressed) && !pressed) {
                    range = last[range].pressed ? range : -range;
                    api._keyup(e, last[range].keyCode, mapped_axis + 256);
                }

                // Update last axis state
                last[range].value = value;
                last[range].pressed = pressed;
            });
        });
    }