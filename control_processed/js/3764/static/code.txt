function _log(message) {
        var level = message.level;
        if (level === "warning") {
            level = "warn";
        }
        var text = "ConsoleAgent: " + message.text;
        if (message.url) {
            text += " (url: " + message.url + ")";
        }
        if (message.stackTrace) {
            var callFrame = message.stackTrace[0];
            text += " in " + callFrame.functionName + ":" + callFrame.columnNumber;
        }
        console[level](text);
    }