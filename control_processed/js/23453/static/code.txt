function(p, callback) {
					var id = p.data.id;
					p.data = null;
					callback('favorites/create.json?id=' + id);
				}