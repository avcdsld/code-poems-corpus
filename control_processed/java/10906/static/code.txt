@Nonnull
    /*package*/ static InputStream getBundledJpiManifestStream(@Nonnull URL url) throws IOException {
        URLConnection uc = url.openConnection();
        InputStream in = null;
        // Magic, which allows to avoid using stream generated for JarURLConnection.
        // It prevents getting into JENKINS-37332 due to the file descriptor leak 
        if (uc instanceof JarURLConnection) {
            final JarURLConnection jarURLConnection = (JarURLConnection) uc;
            final String entryName = jarURLConnection.getEntryName();
            
            try(final JarFile jarFile = jarURLConnection.getJarFile()) {
                final JarEntry entry = (entryName != null && jarFile != null) ? jarFile.getJarEntry(entryName) : null;
                if (entry != null && jarFile != null) {
                    try(InputStream i = jarFile.getInputStream(entry)) {
                        byte[] manifestBytes = IOUtils.toByteArray(i);
                        in = new ByteArrayInputStream(manifestBytes);
                    }
                } else {
                    LOGGER.log(Level.WARNING, "Failed to locate the JAR file for {0}"
                            + "The default URLConnection stream access will be used, file descriptor may be leaked.",
                               url);
                }
            }
        } 

        // If input stream is undefined, use the default implementation
        if (in == null) {
            in = url.openStream();
        }
        
        return in;
    }