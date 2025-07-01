function _updateOverwriteLabel(event, editor, newstate, doNotAnimate) {
        if ($statusOverwrite.text() === (newstate ? Strings.STATUSBAR_OVERWRITE : Strings.STATUSBAR_INSERT)) {
            // label already up-to-date
            return;
        }

        $statusOverwrite.text(newstate ? Strings.STATUSBAR_OVERWRITE : Strings.STATUSBAR_INSERT);

        if (!doNotAnimate) {
            AnimationUtils.animateUsingClass($statusOverwrite[0], "flash", 1500);
        }
    }