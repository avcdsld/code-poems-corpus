function _addBinding(commandID, keyBinding, platform, userBindings) {
        var key,
            result = null,
            normalized,
            normalizedDisplay,
            explicitPlatform = keyBinding.platform || platform,
            targetPlatform,
            command,
            bindingsToDelete = [],
            existing;

        // For platform: "all", use explicit current platform
        if (explicitPlatform && explicitPlatform !== "all") {
            targetPlatform = explicitPlatform;
        } else {
            targetPlatform = brackets.platform;
        }


        // Skip if the key binding is not for this platform.
        if (explicitPlatform === "mac" && brackets.platform !== "mac") {
            return null;
        }

        // if the request does not specify an explicit platform, and we're
        // currently on a mac, then replace Ctrl with Cmd.
        key = (keyBinding.key) || keyBinding;
        if (brackets.platform === "mac" && (explicitPlatform === undefined || explicitPlatform === "all")) {
            key = key.replace("Ctrl", "Cmd");
            if (keyBinding.displayKey !== undefined) {
                keyBinding.displayKey = keyBinding.displayKey.replace("Ctrl", "Cmd");
            }
        }

        normalized = normalizeKeyDescriptorString(key);

        // skip if the key binding is invalid
        if (!normalized) {
            console.error("Unable to parse key binding " + key + ". Permitted modifiers: Ctrl, Cmd, Alt, Opt, Shift; separated by '-' (not '+').");
            return null;
        }

        // check for duplicate key bindings
        existing = _keyMap[normalized];

        // for cross-platform compatibility
        if (exports.useWindowsCompatibleBindings) {
            // windows-only key bindings are used as the default binding
            // only if a default binding wasn't already defined
            if (explicitPlatform === "win") {
                // search for a generic or platform-specific binding if it
                // already exists
                if (existing && (!existing.explicitPlatform ||
                                 existing.explicitPlatform === brackets.platform ||
                                 existing.explicitPlatform === "all")) {
                    // do not clobber existing binding with windows-only binding
                    return null;
                }

                // target this windows binding for the current platform
                targetPlatform = brackets.platform;
            }
        }

        // skip if this binding doesn't match the current platform
        if (targetPlatform !== brackets.platform) {
            return null;
        }

        // skip if the key is already assigned
        if (existing) {
            if (!existing.explicitPlatform && explicitPlatform) {
                // remove the the generic binding to replace with this new platform-specific binding
                removeBinding(normalized);
                existing = false;
            }
        }

        // delete existing bindings when
        // (1) replacing a windows-compatible binding with a generic or
        //     platform-specific binding
        // (2) replacing a generic binding with a platform-specific binding
        var existingBindings = _commandMap[commandID] || [],
            isWindowsCompatible,
            isReplaceGeneric,
            ignoreGeneric;

        existingBindings.forEach(function (binding) {
            // remove windows-only bindings in _commandMap
            isWindowsCompatible = exports.useWindowsCompatibleBindings &&
                binding.explicitPlatform === "win";

            // remove existing generic binding
            isReplaceGeneric = !binding.explicitPlatform &&
                explicitPlatform;

            if (isWindowsCompatible || isReplaceGeneric) {
                bindingsToDelete.push(binding);
            } else {
                // existing binding is platform-specific and the requested binding is generic
                ignoreGeneric = binding.explicitPlatform && !explicitPlatform;
            }
        });

        if (ignoreGeneric) {
            // explicit command binding overrides this one
            return null;
        }

        if (existing) {
            // do not re-assign a key binding
            console.error("Cannot assign " + normalized + " to " + commandID + ". It is already assigned to " + _keyMap[normalized].commandID);
            return null;
        }

        // remove generic or windows-compatible bindings
        bindingsToDelete.forEach(function (binding) {
            removeBinding(binding.key);
        });

        // optional display-friendly string (e.g. CMD-+ instead of CMD-=)
        normalizedDisplay = (keyBinding.displayKey) ? normalizeKeyDescriptorString(keyBinding.displayKey) : normalized;

        // 1-to-many commandID mapping to key binding
        if (!_commandMap[commandID]) {
            _commandMap[commandID] = [];
        }

        result = {
            key                 : normalized,
            displayKey          : normalizedDisplay,
            explicitPlatform    : explicitPlatform
        };

        _commandMap[commandID].push(result);

        // 1-to-1 key binding to commandID
        _keyMap[normalized] = {
            commandID           : commandID,
            key                 : normalized,
            displayKey          : normalizedDisplay,
            explicitPlatform    : explicitPlatform
        };

        if (!userBindings) {
            _updateCommandAndKeyMaps(_keyMap[normalized]);
        }

        // notify listeners
        command = CommandManager.get(commandID);

        if (command) {
            command.trigger("keyBindingAdded", result);
        }

        return result;
    }