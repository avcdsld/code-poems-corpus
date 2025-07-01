function(service, namespace) {
            namespace = namespace || {};
            this._super(service, this.path(), namespace);
            this.create = utils.bind(this, this.create);
        }