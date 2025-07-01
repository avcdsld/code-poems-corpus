function getProjectName(configXml) {
    let output = null;
    if (configXml.widget.hasOwnProperty("name")) {
      const name = configXml.widget.name[0];
      if (typeof name === "string") {
        // handle <name>Branch Cordova</name>
        output = configXml.widget.name[0];
      } else {
        // handle <name short="Branch">Branch Cordova</name>
        output = configXml.widget.name[0]._;
      }
    }

    return output;
  }