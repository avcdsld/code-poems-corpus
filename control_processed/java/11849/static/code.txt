public ComputerLauncher getDelegatedLauncher() {
        ComputerLauncher l = launcher;
        while (true) {
            if (l instanceof DelegatingComputerLauncher) {
                l = ((DelegatingComputerLauncher) l).getLauncher();
            } else if (l instanceof ComputerLauncherFilter) {
                l = ((ComputerLauncherFilter) l).getCore();
            } else {
                break;
            }
        }
        return l;
    }