function() {
  return new Promise(function(resolve, reject) {
    firebase.auth().onAuthStateChanged(function(user) {
      if (user) {
        user.getIdToken().then(function(idToken) {
          resolve(idToken);
        }, function(error) {
          resolve(null);
        });
      } else {
        resolve(null);
      }
    });
  }).catch(function(error) {
    console.log(error);
  });
}