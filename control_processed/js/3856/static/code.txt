function ProjectModel(initial) {
        initial = initial || {};
        if (initial.projectRoot) {
            this.projectRoot = initial.projectRoot;
        }

        if (initial.focused !== undefined) {
            this._focused = initial.focused;
        }
        this._viewModel = new FileTreeViewModel.FileTreeViewModel();
        this._viewModel.on(FileTreeViewModel.EVENT_CHANGE, function () {
            this.trigger(EVENT_CHANGE);
        }.bind(this));
        this._selections = {};
    }