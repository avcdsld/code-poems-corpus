function spliceContentIntoResult(vContent) {
			// equivalent to aResult.apply(start, deleteCount, content1, content2...)
			var args = [i, 1].concat(vContent);
			Array.prototype.splice.apply(aResult, args);
		}