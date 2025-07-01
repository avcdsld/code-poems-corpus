function(props, value, opt) {

        var delim = '/';
        var isString = joint.util.isString(props);

        if (isString || Array.isArray(props)) {
            // Get/set an attribute by a special path syntax that delimits
            // nested objects by the colon character.

            if (arguments.length > 1) {

                var path;
                var pathArray;

                if (isString) {
                    path = props;
                    pathArray = path.split('/');
                } else {
                    path = props.join(delim);
                    pathArray = props.slice();
                }

                var property = pathArray[0];
                var pathArrayLength = pathArray.length;

                opt = opt || {};
                opt.propertyPath = path;
                opt.propertyValue = value;
                opt.propertyPathArray = pathArray;

                if (pathArrayLength === 1) {
                    // Property is not nested. We can simply use `set()`.
                    return this.set(property, value, opt);
                }

                var update = {};
                // Initialize the nested object. Subobjects are either arrays or objects.
                // An empty array is created if the sub-key is an integer. Otherwise, an empty object is created.
                // Note that this imposes a limitation on object keys one can use with Inspector.
                // Pure integer keys will cause issues and are therefore not allowed.
                var initializer = update;
                var prevProperty = property;

                for (var i = 1; i < pathArrayLength; i++) {
                    var pathItem = pathArray[i];
                    var isArrayIndex = Number.isFinite(isString ? Number(pathItem) : pathItem);
                    initializer = initializer[prevProperty] = isArrayIndex ? [] : {};
                    prevProperty = pathItem;
                }

                // Fill update with the `value` on `path`.
                update = joint.util.setByPath(update, pathArray, value, '/');

                var baseAttributes = joint.util.merge({}, this.attributes);
                // if rewrite mode enabled, we replace value referenced by path with
                // the new one (we don't merge).
                opt.rewrite && joint.util.unsetByPath(baseAttributes, path, '/');

                // Merge update with the model attributes.
                var attributes = joint.util.merge(baseAttributes, update);
                // Finally, set the property to the updated attributes.
                return this.set(property, attributes[property], opt);

            } else {

                return joint.util.getByPath(this.attributes, props, delim);
            }
        }

        return this.set(joint.util.merge({}, this.attributes, props), value);
    }