function onChangePassword() {
  var password = $('#changed-password').val();
  activeUser().updatePassword(password).then(function() {
    refreshUserData();
    alertSuccess('Password changed!');
  }, onAuthError);
}