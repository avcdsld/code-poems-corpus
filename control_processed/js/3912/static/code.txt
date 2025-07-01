function get(command) {
        var commandID;
        if (!command) {
            console.error("Attempting to get a Sort method with a missing required parameter: command");
            return;
        }

        if (typeof command === "string") {
            commandID = command;
        } else {
            commandID = command.getID();
        }
        return _sorts[commandID];
    }