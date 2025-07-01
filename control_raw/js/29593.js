function isAdmin(options, username) {
	return (options.configParams.get("orion.auth.user.creation") || "").split(",").some(function(user) {
		return user === username;
	});
}