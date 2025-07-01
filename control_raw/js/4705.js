function makeUrlsRelativeToCss(match, quotationMark, url) {
            if (PathUtils.isRelativeUrl(url)) {
                var absUrl = PathUtils.makeUrlAbsolute(url, docUrl);
                return "url(" + quotationMark + absUrl + quotationMark + ")";
            }
            return match;
        }