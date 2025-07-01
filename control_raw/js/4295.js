function checkInstallerStatus(requester, searchParams) {
        var installErrorStr = searchParams.installErrorStr,
            bracketsErrorStr = searchParams.bracketsErrorStr,
            updateDirectory = searchParams.updateDir,
            encoding =        searchParams.encoding || "utf8",
            statusObj = {installError: ": BA_UN"},
            logFileAvailable = false,
            currentRequester = requester || "";

        var notifyBrackets = function notifyBrackets(errorline) {
            statusObj.installError = errorline || ": BA_UN";
            postMessageToBrackets(MessageIds.NOTIFY_INSTALLATION_STATUS, currentRequester, statusObj);
        };

        var parseLog = function (files) {
            files.forEach(function (file) {
                var fileExt = path.extname(path.basename(file));
                if (fileExt === ".logs") {
                    var fileName = path.basename(file),
                        fileFullPath = updateDirectory + '/' + file;
                    if (fileName.search("installStatus.logs") !== -1) {
                        logFileAvailable = true;
                        parseInstallerLog(fileFullPath, bracketsErrorStr, "utf8", notifyBrackets);
                    } else if (fileName.search("update.logs") !== -1) {
                        logFileAvailable = true;
                        parseInstallerLog(fileFullPath, installErrorStr, encoding, notifyBrackets);
                    }
                }
            });
            if (!logFileAvailable) {
                postMessageToBrackets(MessageIds.NOTIFY_INSTALLATION_STATUS, currentRequester, statusObj);
            }
        };

        fs.readdir(updateDirectory)
            .then(function (files) {
                return parseLog(files);
            }).catch(function () {
                postMessageToBrackets(MessageIds.NOTIFY_INSTALLATION_STATUS, currentRequester, statusObj);
            });
    }