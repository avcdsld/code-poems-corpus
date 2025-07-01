function(element, options) {
        this.name = name;
        this.$ = $(element);
        this.isTable = (this.$[0].tagName === 'TABLE');
        this.firstShow = true;
        if(this.isTable) {
            this.$table = this.$;
            this.id = 'datatable-' + (this.$.attr('id') || $.zui.uuid());
        } else {
            this.$datatable = this.$.addClass('datatable');
            if(this.$.attr('id')) {
                this.id = this.$.attr('id');
            } else {
                this.id = 'datatable-' + $.zui.uuid();
                this.$.attr('id', this.id);
            }
        }
        this.getOptions(options);
        this.load();

        this.callEvent('ready');
    }