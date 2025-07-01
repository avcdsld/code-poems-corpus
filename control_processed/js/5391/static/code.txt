function onSignInWithEmailAndPassword() {
  var email = $('#signin-email').val();
  var password = $('#signin-password').val();
  auth.signInWithEmailAndPassword(email, password)
      .then(onAuthUserCredentialSuccess, onAuthError);
}