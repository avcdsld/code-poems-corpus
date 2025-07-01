function () {
        var enabledAttributes = this._enabledAttributes;
        var attributeList = this._attributeList;
        // Cache
        if (enabledAttributes) {
            return enabledAttributes;
        }

        var result = [];
        var nVertex = this.vertexCount;

        for (var i = 0; i < attributeList.length; i++) {
            var name = attributeList[i];
            var attrib = this.attributes[name];
            if (attrib.value) {
                if (attrib.value.length === nVertex * attrib.size) {
                    result.push(name);
                }
            }
        }

        this._enabledAttributes = result;

        return result;
    }