function initClient() {

    var scope =
        "https://www.googleapis.com/auth/cloud-platform " +
        "https://www.googleapis.com/auth/genomics " +
        "https://www.googleapis.com/auth/devstorage.read_only " +
        "https://www.googleapis.com/auth/userinfo.profile " +
        "https://www.googleapis.com/auth/drive.readonly";

    igv.google.loadGoogleProperties("https://s3.amazonaws.com/igv.org.app/web_client_google")

        .then(function (properties) {

            var foo = {
                'clientId': properties["client_id"],
                'scope': scope

            };

            return gapi.client.init(foo);
        })
        .then(function () {

            gapi.signin2.render('signInButton', {
                'scope': scope,
                'width': 120,
                'height': 30,
                'longtitle': false,
                'theme': 'dark',
                'onsuccess': handleSignInClick,
                'onfailure': function (error) {
                    console.log(error)
                }
            });

            var div, options, browser;

            div = $("#myDiv")[0];
            options = {

                genome: "hg19",
                locus: 'myc',
                apiKey: igv.google.properties["api_key"],
            };

            browser = igv.createBrowser(div, options);

            gapi.auth2.getAuthInstance().isSignedIn.listen(updateSigninStatus);
        })


    function handleSignInClick(event) {
        // Nothing to do
    }

    function updateSigninStatus(isSignedIn) {

        const user = gapi.auth2.getAuthInstance().currentUser.get();
        const token = user.getAuthResponse().access_token;
        igv.oauth.google.setToken(token);
       // igv.oauth.setToken(token, "*googleapis*");
    }

}