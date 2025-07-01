protected void addPathFile(File pathComponent) throws IOException {
        if (!pathComponents.contains(pathComponent)) {
            pathComponents.addElement(pathComponent);
        }
        if (pathComponent.isDirectory()) {
            return;
        }

        String absPathPlusTimeAndLength = pathComponent.getAbsolutePath()
                + pathComponent.lastModified() + "-" + pathComponent.length();
        String classpath = (String) pathMap.get(absPathPlusTimeAndLength);
        if (classpath == null) {
            JarFile jarFile = null;
            try {
                jarFile = new JarFile(pathComponent);
                Manifest manifest = jarFile.getManifest();
                if (manifest == null) {
                    return;
                }
                classpath = manifest.getMainAttributes()
                    .getValue(Attributes.Name.CLASS_PATH);
            } finally {
                if (jarFile != null) {
                    jarFile.close();
                }
            }
            if (classpath == null) {
                classpath = "";
            }
            pathMap.put(absPathPlusTimeAndLength, classpath);
        }

        if (!"".equals(classpath)) {
            URL baseURL = FILE_UTILS.getFileURL(pathComponent);
            StringTokenizer st = new StringTokenizer(classpath);
            while (st.hasMoreTokens()) {
                String classpathElement = st.nextToken();
                URL libraryURL = new URL(baseURL, classpathElement);
                if (!libraryURL.getProtocol().equals("file")) {
                    log("Skipping jar library " + classpathElement
                            + " since only relative URLs are supported by this" + " loader",
                            Project.MSG_VERBOSE);
                    continue;
                }
                String decodedPath = Locator.decodeUri(libraryURL.getFile());
                File libraryFile = new File(decodedPath);
                if (libraryFile.exists() && !isInPath(libraryFile)) {
                    addPathFile(libraryFile);
                }
            }
        }
    }