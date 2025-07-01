function(parent, key) {
        this.parent = this.parent || parent;
        this.key = this.key || key;
        if (this.parent !== parent) {
          throw new Error(
            'Internal Error. Relation retrieved from two different Objects.'
          );
        }
        if (this.key !== key) {
          throw new Error(
            'Internal Error. Relation retrieved from two different keys.'
          );
        }
      }