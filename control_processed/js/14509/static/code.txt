function getChildAt(index) {
         if (index >= 0 && index < this.children.length) {
           return this.children[index];
         } else {
           throw new Error("Index (" + index + ") Out Of Bounds for getChildAt()");
         }
       }