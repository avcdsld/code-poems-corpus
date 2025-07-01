function (selected) {
        if (selected) {
            this.setRegion(this.on_icon_region);
            this.isSelected = true;
        } else {
            this.setRegion(this.off_icon_region);
            this.isSelected = false;
        }
    }