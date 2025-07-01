function (oControl) {
			var sFlexReference = Utils.getComponentClassName(oControl);
			var oAppComponent = Utils.getAppComponentForControl(oControl);
			var sComponentName = Utils.getComponentName(oAppComponent);
			return sFlexReference !== sComponentName;
		}