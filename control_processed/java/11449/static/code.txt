static void relocateOldLogs(File dir) {
        final Pattern logfile = Pattern.compile("slave-(.*)\\.log(\\.[0-9]+)?");
        File[] logfiles = dir.listFiles(new FilenameFilter() {
            public boolean accept(File dir, String name) {
                return logfile.matcher(name).matches();
            }
        });
        if (logfiles==null)     return;

        for (File f : logfiles) {
            Matcher m = logfile.matcher(f.getName());
            if (m.matches()) {
                File newLocation = new File(dir, "logs/slaves/" + m.group(1) + "/slave.log" + Util.fixNull(m.group(2)));
                newLocation.getParentFile().mkdirs();
                boolean relocationSuccessful=f.renameTo(newLocation);
                if (relocationSuccessful) { // The operation will fail if mkdir fails
                    LOGGER.log(Level.INFO, "Relocated log file {0} to {1}",new Object[] {f.getPath(),newLocation.getPath()});
                } else {
                    LOGGER.log(Level.WARNING, "Cannot relocate log file {0} to {1}",new Object[] {f.getPath(),newLocation.getPath()});
                }
            } else {
                assert false;
            }
        }
    }