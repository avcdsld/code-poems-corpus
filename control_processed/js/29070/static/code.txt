function(user) {
        var promise;
        if (AV.User._currentUser !== user) {
          promise = AV.User.logOut();
        } else {
          promise = Promise.resolve();
        }
        return promise.then(function() {
          user._isCurrentUser = true;
          AV.User._currentUser = user;

          var json = user._toFullJSON();
          json._id = user.id;
          json._sessionToken = user._sessionToken;
          return AV.localStorage
            .setItemAsync(
              AV._getAVPath(AV.User._CURRENT_USER_KEY),
              JSON.stringify(json)
            )
            .then(function() {
              AV.User._currentUserMatchesDisk = true;
              return AV._refreshSubscriptionId();
            });
        });
      }