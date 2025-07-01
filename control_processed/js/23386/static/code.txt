function(name, value) {
			if (name == value) {
				return true;
			}

			var boolAttrs = prefs.get('profile.booleanAttributes');
			if (!value && boolAttrs) {
				boolAttrs = new RegExp(boolAttrs, 'i');
				return boolAttrs.test(name);
			}

			return false;
		}