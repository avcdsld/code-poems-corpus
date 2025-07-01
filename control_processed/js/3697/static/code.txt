function formatError(error) {
        function localize(key) {
            if (Strings[key]) {
                return Strings[key];
            }
            console.log("Unknown installation error", key);
            return Strings.UNKNOWN_ERROR;
        }

        if (Array.isArray(error)) {
            error[0] = localize(error[0]);
            return StringUtils.format.apply(window, error);
        } else {
            return localize(error);
        }
    }