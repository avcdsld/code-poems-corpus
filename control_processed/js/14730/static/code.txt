function (/* event */) {
        if (!me.device.isFullscreen) {
            me.device.requestFullscreen();
        } else {
            me.device.exitFullscreen();
        }
        return false;
    }