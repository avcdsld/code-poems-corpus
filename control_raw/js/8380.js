function resolveBinding(sBinding, oModel, sPath) {
			if (!sBinding) {
				return sBinding;
			}
			var oBindingInfo = ManagedObject.bindingParser(sBinding);

			if (!oBindingInfo) {
				return sBinding;
			}

			if (!sPath) {
				sPath = "/";
			}

			oSimpleControl.setModel(oModel);
			oSimpleControl.bindObject(sPath);
			oSimpleControl.bindProperty("resolved", oBindingInfo);

			var vValue = oSimpleControl.getResolved();

			oSimpleControl.unbindProperty("resolved");
			oSimpleControl.unbindObject();
			oSimpleControl.setModel(null);

			return vValue;
		}