function addChildAt(child, index) {
         if (index >= 0 && index < this.children.length) {
           if (child.ancestor instanceof me.Container) {
             child.ancestor.removeChildNow(child);
           } else {
             // only allocate a GUID if the object has no previous ancestor
             // (e.g. move one child from one container to another)
             if (child.isRenderable) {
               // allocated a GUID value
               child.GUID = me.utils.createGUID();
             }
           }

           child.ancestor = this;
           this.children.splice(index, 0, child);

           if (typeof child.onActivateEvent === "function" && this.isAttachedToRoot()) {
             child.onActivateEvent();
           }

           this.onChildChange.call(this, index);
           return child;
         } else {
           throw new Error("Index (" + index + ") Out Of Bounds for addChildAt()");
         }
       }