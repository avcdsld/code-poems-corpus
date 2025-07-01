function formatDate(lang, input) {

	var result = input;
	var matches;
	var localeDateString;

	while ((matches = DATE_REGEX.exec(input)) != null) {

		var date = new Date(Date.parse(matches[1]));
		var format = matches[2] != undefined ? matches[2].toLowerCase() : "compact";

		if (format != "compact") {
			localeDateString = date.toLocaleDateString(lang,
				{
					day: "numeric",
					weekday: format,
					month: format,
					year: "numeric"
				});
		}
		else {
			localeDateString = date.toLocaleDateString();
		}
		result = result.replace(matches[0], localeDateString);
	};
	return result;

}