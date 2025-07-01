function(feature) {

        var interactive = joint.util.isFunction(this.options.interactive)
            ? this.options.interactive(this)
            : this.options.interactive;

        return (joint.util.isObject(interactive) && interactive[feature] !== false) ||
                (joint.util.isBoolean(interactive) && interactive !== false);
    }