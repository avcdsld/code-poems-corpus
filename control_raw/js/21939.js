function (level, message) {
            if (message && level > 0 && level <= loggingLevel) {
                if (level === Logger.LEVEL_SEVERE) {
                    console.error(message);
                } else if (level === Logger.LEVEL_WARNING) {
                    console.warn(message);
                } else if (level === Logger.LEVEL_INFO) {
                    console.info(message);
                } else {
                    console.log(message);
                }
            }
        }