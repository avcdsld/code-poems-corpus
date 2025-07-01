function getVersionWithoutSuffix(sVersion) {
		var oVersion = Version(sVersion);
		return oVersion.getSuffix() ? Version(oVersion.getMajor() + "." + oVersion.getMinor() + "." + oVersion.getPatch()) : oVersion;
	}