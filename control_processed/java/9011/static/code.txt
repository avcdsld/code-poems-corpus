public URLNormalizer sortQueryParameters() {
        // Does it have query parameters?
        if (!url.contains("?")) {
            return this;
        }
        // It does, so proceed
        List<String> keyValues = new ArrayList<>();
        String queryString = StringUtils.substringAfter(url, "?");

        // extract and remove any fragments
        String fragment = StringUtils.substringAfter(queryString, "#");
        if (StringUtils.isNotBlank(fragment)) {
            fragment = "#" + fragment;
        }
        queryString = StringUtils.substringBefore(queryString, "#");

        String[] params = StringUtils.split(queryString, '&');
        for (String param : params) {
            keyValues.add(param);
        }
        // sort it so that query string are in order
        Collections.sort(keyValues);

        String sortedQueryString = StringUtils.join(keyValues, '&');
        if (StringUtils.isNotBlank(sortedQueryString)) {
            url = StringUtils.substringBefore(
                    url, "?") + "?" + sortedQueryString + fragment;
        }

        return this;
    }