function(password) {
      var user = this.getAuth();
      if (user) {
        return this._q.when(user.updatePassword(password));
      } else {
        return this._q.reject("Cannot update password since there is no logged in user.");
      }
    }