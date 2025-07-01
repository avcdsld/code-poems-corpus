function hotDownloadManifest() {
		var filename = require("path").join(__dirname, $hotMainFilename$);
		return new Promise(function(resolve, reject) {
			require("fs").readFile(filename, "utf-8", function(err, content) {
				if (err) return resolve();
				try {
					var update = JSON.parse(content);
				} catch (e) {
					return reject(e);
				}
				resolve(update);
			});
		});
	}