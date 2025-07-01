private URL getUrl() {
        ClassLoader loader = null;
        try {
            loader = Thread.currentThread().getContextClassLoader();
        } catch (Exception e) {
            // do nothing
        }

        if (loader == null) {
            loader = ClassPathResource.class.getClassLoader();
        }

        URL url = loader.getResource(this.resourceName);
        if (url == null) {
            // try to check for mis-used starting slash
            // TODO: see TODO below
            if (this.resourceName.startsWith("/")) {
                url = loader.getResource(this.resourceName.replaceFirst("[\\\\/]", ""));
                if (url != null)
                    return url;
            } else {
                // try to add slash, to make clear it's not an issue
                // TODO: change this mechanic to actual path purifier
                url = loader.getResource("/" + this.resourceName);
                if (url != null)
                    return url;
            }
            throw new IllegalStateException("Resource '" + this.resourceName + "' cannot be found.");
        }
        return url;
    }