public void setDialogContainer(StackPane dialogContainer) {
        if (dialogContainer != null) {
            this.dialogContainer = dialogContainer;
            // FIXME: need to be improved to consider only the parent boundary
            offsetX = dialogContainer.getBoundsInLocal().getWidth();
            offsetY = dialogContainer.getBoundsInLocal().getHeight();
            animation = getShowAnimation(transitionType.get());
        }
    }