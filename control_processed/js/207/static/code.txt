function(node) {
      var range = rangy.createRange(this.doc);

      range.setStartAfter(node);
      range.setEndAfter(node);
      return this.setSelection(range);
    }