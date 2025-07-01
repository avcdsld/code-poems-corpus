function() {
      var mimeTypeList = "";

      for (var i = 0; i < navigator.mimeTypes.length; i++) {
        if (i == navigator.mimeTypes.length - 1) {
          mimeTypeList += navigator.mimeTypes[i].description;
        } else {
          mimeTypeList += navigator.mimeTypes[i].description + ", ";
        }
      }
      return mimeTypeList;
    }