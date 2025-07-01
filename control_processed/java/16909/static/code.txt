public void activateFrame(@NonNull String frameName, boolean reallyActivate) {
        frames.get(frameName).setActive(reallyActivate);
    }