function (str) {
      var strlen = str.length;
      if (this.html.substr(this.currentChar, strlen).toLowerCase() === str.toLowerCase()) {
        this.currentChar += strlen;
        return true;
      }
      return false;
    }