function refreshUserData() {
  if (activeUser()) {
    var user = activeUser();
    $('.profile').show();
    $('body').addClass('user-info-displayed');
    $('div.profile-email,span.profile-email').text(user.email || 'No Email');
    $('div.profile-phone,span.profile-phone')
        .text(user.phoneNumber || 'No Phone');
    $('div.profile-uid,span.profile-uid').text(user.uid);
    $('div.profile-name,span.profile-name').text(user.displayName || 'No Name');
    $('input.profile-name').val(user.displayName);
    $('input.photo-url').val(user.photoURL);
    if (user.photoURL != null) {
      var photoURL = user.photoURL;
      // Append size to the photo URL for Google hosted images to avoid requesting
      // the image with its original resolution (using more bandwidth than needed)
      // when it is going to be presented in smaller size.
      if ((photoURL.indexOf('googleusercontent.com') != -1) ||
          (photoURL.indexOf('ggpht.com') != -1)) {
        photoURL = photoURL + '?sz=' + $('img.profile-image').height();
      }
      $('img.profile-image').attr('src', photoURL).show();
    } else {
      $('img.profile-image').hide();
    }
    $('.profile-email-verified').toggle(user.emailVerified);
    $('.profile-email-not-verified').toggle(!user.emailVerified);
    $('.profile-anonymous').toggle(user.isAnonymous);
    // Display/Hide providers icons.
    $('.profile-providers').empty();
    if (user['providerData'] && user['providerData'].length) {
      var providersCount = user['providerData'].length;
      for (var i = 0; i < providersCount; i++) {
        addProviderIcon(user['providerData'][i]['providerId']);
      }
    }
    // Change color.
    if (user == auth.currentUser) {
      $('#user-info').removeClass('last-user');
      $('#user-info').addClass('current-user');
    }  else {
      $('#user-info').removeClass('current-user');
      $('#user-info').addClass('last-user');
    }
  } else {
    $('.profile').slideUp();
    $('body').removeClass('user-info-displayed');
    $('input.profile-data').val('');
  }
}