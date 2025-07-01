function(username, password, attrs, options) {
        attrs = attrs || {};
        attrs.username = username;
        attrs.password = password;
        var user = AV.Object._create('_User');
        return user.signUp(attrs, options);
      }