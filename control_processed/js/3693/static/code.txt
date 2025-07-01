function githubURLFilter(urlInfo) {
        if (urlInfo.parsed.hostname === "github.com" || urlInfo.parsed.hostname === "www.github.com") {
            // Is it a URL to the root of a repo? (/user/repo)
            var match = /^\/[^\/?]+\/([^\/?]+)(\/?)$/.exec(urlInfo.parsed.pathname);
            if (match) {
                if (!match[2]) {
                    urlInfo.url += "/";
                }
                urlInfo.url += "archive/master.zip";
                urlInfo.filenameHint = match[1] + ".zip";

            } else {
                // Is it a URL directly to the repo's 'master.zip'? (/user/repo/archive/master.zip)
                match = /^\/[^\/?]+\/([^\/?]+)\/archive\/master.zip$/.exec(urlInfo.parsed.pathname);
                if (match) {
                    urlInfo.filenameHint = match[1] + ".zip";
                }
            }
        }
    }