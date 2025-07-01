function(name, collection) {
			if (collection in elementTypes) {
				elementTypes[collection] = utils.without(this.getCollection(collection), name);
			}
		}