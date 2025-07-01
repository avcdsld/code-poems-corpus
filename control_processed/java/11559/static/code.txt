public static boolean isDefaultJDKValid(Node n) {
        try {
            TaskListener listener = new StreamTaskListener(new NullStream());
            Launcher launcher = n.createLauncher(listener);
            return launcher.launch().cmds("java","-fullversion").stdout(listener).join()==0;
        } catch (IOException | InterruptedException e) {
            return false;
        }
    }