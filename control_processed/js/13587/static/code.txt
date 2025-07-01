function () {
        var node = new this.constructor();

        var children = this._children;

        node.setName(this.name);
        node.position.copy(this.position);
        node.rotation.copy(this.rotation);
        node.scale.copy(this.scale);

        for (var i = 0; i < children.length; i++) {
            node.add(children[i].clone());
        }

        return node;
    }