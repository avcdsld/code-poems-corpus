function watchPrefsForChanges() {
        prefs.prefsObject.on("change", function (e, data) {
            if (data.ids.indexOf("enabled") > -1) {
                // Check if enabled state mismatches whether code-folding is actually initialized (can't assume
                // since preference change events can occur when the value hasn't really changed)
                var isEnabled = prefs.getSetting("enabled");
                if (isEnabled && !_isInitialized) {
                    init();
                } else if (!isEnabled && _isInitialized) {
                    deinit();
                }
            }
        });
    }