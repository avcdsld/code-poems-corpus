public String getNormalisedPrefix() {
        StringBuilder strBuilder = new StringBuilder();
        strBuilder.append(scheme).append("://").append(host);
        if (!isDefaultHttpOrHttpsPort(scheme, port)) {
            strBuilder.append(':').append(port);
        }
        if (path != null) {
            strBuilder.append(path);
        }
        return strBuilder.toString();
    }