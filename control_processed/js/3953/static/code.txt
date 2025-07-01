function handleError(message, url, line) {
        // Ignore this error if it does not look like the rather vague cross origin error in Chrome
        // Chrome will print it to the console anyway
        if (!testCrossOriginError(message, url, line)) {
            if (previousErrorHandler) {
                return previousErrorHandler(message, url, line);
            }
            return;
        }

        // Show an error message
        window.alert("Oops! This application doesn't run in browsers yet.\n\nIt is built in HTML, but right now it runs as a desktop app so you can use it to edit local files. Please use the application shell in the following repo to run this application:\n\ngithub.com/adobe/brackets-shell");

        // Restore the original handler for later errors
        window.onerror = previousErrorHandler;
    }