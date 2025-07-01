function registrationIds() {
			const ids = [];
			for (const regid of findChildren(sapFioriAppData, "registrationId")) {
				ids.push(regid._);
			}
			return ids.length > 0 ? ids : undefined;
		}