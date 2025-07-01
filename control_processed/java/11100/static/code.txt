private void updateJenkinsExeIfNeeded() {
        try {
            File baseDir = getBaseDir();

            URL exe = getClass().getResource("/windows-service/jenkins.exe");
            String ourCopy = Util.getDigestOf(exe.openStream());

            for (String name : new String[]{"hudson.exe","jenkins.exe"}) {
                try {
                    File currentCopy = new File(baseDir,name);
                    if(!currentCopy.exists())   continue;
                    String curCopy = new FilePath(currentCopy).digest();

                    if(ourCopy.equals(curCopy))     continue; // identical

                    File stage = new File(baseDir,name+".new");
                    FileUtils.copyURLToFile(exe,stage);
                    Kernel32.INSTANCE.MoveFileExA(stage.getAbsolutePath(),currentCopy.getAbsolutePath(),MOVEFILE_DELAY_UNTIL_REBOOT|MOVEFILE_REPLACE_EXISTING);
                    LOGGER.info("Scheduled a replacement of "+name);
                } catch (IOException e) {
                    LOGGER.log(Level.SEVERE, "Failed to replace "+name,e);
                } catch (InterruptedException e) {
                }
            }
        } catch (IOException e) {
            LOGGER.log(Level.SEVERE, "Failed to replace jenkins.exe",e);
        }
    }