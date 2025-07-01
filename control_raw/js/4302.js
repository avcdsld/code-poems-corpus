function init(domainManager) {
        if (!domainManager.hasDomain("AutoUpdate")) {
            domainManager.registerDomain("AutoUpdate", {
                major: 0,
                minor: 1
            });
        }
        _domainManager = domainManager;

        domainManager.registerCommand(
            "AutoUpdate",
            "initNode",
            initNode,
            true,
            "Initializes node for the auto update",
            [
                {
                    name: "initObj",
                    type: "object",
                    description: "json object containing init information"
                }
            ],
            []
        );

        domainManager.registerCommand(
            "AutoUpdate",
            "data",
            receiveMessageFromBrackets,
            true,
            "Receives messages from brackets",
            [
                {
                    name: "msgObj",
                    type: "object",
                    description: "json object containing message info"
                }
            ],
            []
        );

        domainManager.registerEvent(
            "AutoUpdate",
            "data",
            [
                {
                    name: "msgObj",
                    type: "object",
                    description: "json object containing message info to pass to brackets"
                }
            ]
        );
    }