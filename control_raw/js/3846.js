function ExtensionManagerViewModel() {
        this._handleStatusChange = this._handleStatusChange.bind(this);

        // Listen for extension status changes.
        ExtensionManager
            .on("statusChange." + this.source, this._handleStatusChange)
            .on("registryUpdate." + this.source, this._handleStatusChange);
    }