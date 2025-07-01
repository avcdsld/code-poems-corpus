function toggleSizeClasses(iSize) {
		var sCurrentSizeClass = 'sapMSize' + iSize,
			oRef = this.$(),
			i,
			sClass;

		if (oRef) {
			for (i = 0; i < 3; i++) {
				sClass = 'sapMSize' + i;
				if (sClass === sCurrentSizeClass) {
					oRef.addClass(sClass);
				} else {
					oRef.removeClass(sClass);
				}
			}
		}
	}