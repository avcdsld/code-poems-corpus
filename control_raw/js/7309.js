function(oOldOptions, oNewOptions) {

			var oMergedOptions = jQuery.extend({}, oOldOptions, oNewOptions);

			jQuery.each(oMergedOptions, function(key) {
				oMergedOptions[key] = oOldOptions[key] || oNewOptions[key]; // default merge strategy is inclusive OR
			});
			return oMergedOptions;
		}