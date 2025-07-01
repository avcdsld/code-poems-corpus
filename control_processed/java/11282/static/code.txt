@Override
    public synchronized void save() {
        if(areStatsDisabled()){
            return;
        }
        
        if (BulkChange.contains(this))
            return;
        
        /*
         * Note: the userFolder should never be null at this point.
         * The userFolder could be null during User creation with the new storage approach
         * but when this code is called, from token used / removed, the folder exists.
         */
        File userFolder = getUserFolder();
        if (userFolder == null) {
            return;
        }
        
        XmlFile configFile = getConfigFile(userFolder);
        try {
            configFile.write(this);
            SaveableListener.fireOnChange(this, configFile);
        } catch (IOException e) {
            LOGGER.log(Level.WARNING, "Failed to save " + configFile, e);
        }
    }