function(element, options) {
        this.$element = $(element)
        this.options = $.extend({}, Collapse.DEFAULTS, options)
        this.transitioning = null

        if(this.options.parent) this.$parent = $(this.options.parent)
        if(this.options.toggle) this.toggle()
    }