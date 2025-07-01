function Annotatable(oConverter, sTarget) {
		var oParent = oConverter.oAnnotatable;

		if (oParent) {
			sTarget = _Helper.buildPath(oParent.sPath, sTarget);
		}
		this.oConverter = oConverter;
		this.sPath = sTarget;
		this.oParent = oParent;
		this.mSapAttributes = oConverter.mSapAttributes;
		this.mAnnotationsForTarget = null;
	}