function onLinkReauthVerifyPhoneNumber() {
  var phoneNumber = $('#link-reauth-phone-number').val();
  var provider = new firebase.auth.PhoneAuthProvider(auth);
  // Clear existing reCAPTCHA as an existing reCAPTCHA could be targeted for a
  // sign-in operation.
  clearApplicationVerifier();
  // Initialize a reCAPTCHA application verifier.
  makeApplicationVerifier('link-reauth-verify-phone-number');
  provider.verifyPhoneNumber(phoneNumber, applicationVerifier)
      .then(function(verificationId) {
        clearApplicationVerifier();
        $('#link-reauth-phone-verification-id').val(verificationId);
        alertSuccess('Phone verification sent!');
      }, function(error) {
        clearApplicationVerifier();
        onAuthError(error);
      });
}