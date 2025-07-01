function (node) {
      var name = "";

      var n = this.html.indexOf("=", this.currentChar);
      if (n === -1) {
        this.currentChar = this.html.length;
      } else {
        // Read until a '=' character is hit; this will be the attribute key
        name = this.html.substring(this.currentChar, n);
        this.currentChar = n + 1;
      }

      if (!name)
        return;

      // After a '=', we should see a '"' for the attribute value
      var c = this.nextChar();
      if (c !== '"' && c !== "'") {
        this.error("Error reading attribute " + name + ", expecting '\"'");
        return;
      }

      // Read the attribute value (and consume the matching quote)
      var value = this.readString(c);

      node.attributes.push(new Attribute(name, value));

      return;
    }