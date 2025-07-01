function getModuleUrl(module, path) {
        var url = encodeURI(getModulePath(module, path));

        // On Windows, $.get() fails if the url is a full pathname. To work around this,
        // prepend "file:///". On the Mac, $.get() works fine if the url is a full pathname,
        // but *doesn't* work if it is prepended with "file://". Go figure.
        // However, the prefix "file://localhost" does work.
        if (brackets.platform === "win" && url.indexOf(":") !== -1) {
            url = "file:///" + url;
        }

        return url;
    }