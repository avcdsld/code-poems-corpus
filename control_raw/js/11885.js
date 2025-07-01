function() {
        var factory = this.viewFactory;

        this._addChildren([
            factory.createFrame(frameConst.L),
            factory.createFrame(frameConst.R)
        ]);
    }