public void doResources(StaplerRequest req, StaplerResponse rsp) throws IOException, ServletException {
        String path = req.getRestOfPath();
        // cut off the "..." portion of /resources/.../path/to/file
        // as this is only used to make path unique (which in turn
        // allows us to set a long expiration date
        path = path.substring(path.indexOf('/',1)+1);

        int idx = path.lastIndexOf('.');
        String extension = path.substring(idx+1);
        if(ALLOWED_RESOURCE_EXTENSIONS.contains(extension)) {
            URL url = pluginManager.uberClassLoader.getResource(path);
            if(url!=null) {
                long expires = MetaClass.NO_CACHE ? 0 : TimeUnit.DAYS.toMillis(365);
                rsp.serveFile(req,url,expires);
                return;
            }
        }
        rsp.sendError(HttpServletResponse.SC_NOT_FOUND);
    }