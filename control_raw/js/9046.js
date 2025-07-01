function () {

			var aFilters = [],
				aSorters = [],
				bFilterChanged = false,
				bGroupChanged = false,
				oSearchField = this.byId("searchField"),
				oList = this.byId("list"),
				oBinding = oList.getBinding("items");

			// add filter for search
			var sQuery = oSearchField.getValue().trim();

			bFilterChanged = true;
			aFilters.push(new Filter("searchTags", "Contains", sQuery));

			// add filters for view settings
			jQuery.each(this._oViewSettings.filter, function (sProperty, aValues) {
				var aPropertyFilters = [];
				jQuery.each(aValues, function (i, aValue) {
					var sOperator = (sProperty === "formFactors") ? "Contains" : "EQ";
					aPropertyFilters.push(new Filter(sProperty, sOperator, aValue));
				});
				var oFilter = new Filter(aPropertyFilters, false); // second parameter stands for "or"
				bFilterChanged = true;
				aFilters.push(oFilter);
			});

			// filter
			if (bFilterChanged && aFilters.length === 0) {
				oBinding.filter(aFilters, "Application");
			} else if (bFilterChanged && aFilters.length > 0) {
				var oFilter = new Filter(aFilters, true); // second parameter stands for "and"
				oBinding.filter(oFilter, "Application");
			}

			if (this._oViewSettings.groupProperty && this._oViewSettings.groupProperty !== this._sCurrentGroup) {
				bGroupChanged = true;
			} else if (this._oViewSettings.groupProperty && this._oViewSettings.groupDescending !== this._bCurrentlyGroupedDescending) {
				bGroupChanged = true;
			}

			// group
			if (bGroupChanged) {
				var oSorter = new Sorter(
					this._oViewSettings.groupProperty,
					this._oViewSettings.groupDescending,
					this._mGroupFunctions[this._oViewSettings.groupProperty]);
				aSorters.push(oSorter);
				aSorters.push(new Sorter("name", false));
				oBinding.sort(aSorters);
			}

			this._sCurrentGroup = this._oViewSettings.groupProperty;
			this._bCurrentlyGroupedDescending = this._oViewSettings.groupDescending;

			// memorize that this function was executed at least once
			this._bIsViewUpdatedAtLeastOnce = true;
		}