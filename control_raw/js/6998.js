function showNotification(msg, type, reloadPage){
    // defaults to false
    reloadPage = reloadPage || false;

    $('#notify_message').removeClass();
    $('#notify_message').addClass('alert-' + type);
    $('#notify_message').html(msg);
    $('#notify_message').slideDown(600).delay(2500).slideUp(600, function(){
        if(reloadPage === true){
            location.reload();
        }
    });
}