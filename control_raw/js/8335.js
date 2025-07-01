function _getFrameworkName() {
			var versionInfo;
			var frameworkInfo;

			try {
				versionInfo = sap.ui.getVersionInfo();
			} catch (e) {
				versionInfo = undefined;
			}

			if (versionInfo) {
				// Use group artifact version for maven builds or name for other builds (like SAPUI5-on-ABAP)
				frameworkInfo = versionInfo.gav ? versionInfo.gav : versionInfo.name;

				return frameworkInfo.indexOf('openui5') !== -1 ? 'OpenUI5' : 'SAPUI5';
			} else {
				return '';
			}
		}