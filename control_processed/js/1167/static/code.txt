function hotDownloadUpdateChunk(chunkId) {
		var filename = require("path").join(__dirname, $hotChunkFilename$);
		require("fs").readFile(filename, "utf-8", function(err, content) {
			if (err) {
				if ($require$.onError) return $require$.oe(err);
				throw err;
			}
			var chunk = {};
			require("vm").runInThisContext(
				"(function(exports) {" + content + "\n})",
				{ filename: filename }
			)(chunk);
			hotAddUpdateChunk(chunk.id, chunk.modules);
		});
	}