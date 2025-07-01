function send() {
		// Check form for errors
		if(!$("#transaction").val()) return alert('Missing parameter !');

		// Send
		nem.com.requests.transaction.announce(endpoint, $("#transaction").val()).then(function(res) {
			// If code >= 2, it's an error
			if (res.code >= 2) {
				alert(res.message);
			} else {
				alert(res.message);
			}
		}, function(err) {
			alert(err);
		})
	}