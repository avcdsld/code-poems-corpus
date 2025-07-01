function() {
			// Converting the row height CSS parameters (e.g. _sap_ui_table_RowHeight) is too complex (CSS calc()).
			// Therefore, the base sizes are used and calculation is done in JavaScript.

			function getPixelValue(sThemeParameterName) {
				return TableUtils.convertCSSSizeToPixel(ThemeParameters.get(sThemeParameterName));
			}

			mBaseSize.undefined = getPixelValue("_sap_ui_table_BaseSize");
			mBaseSize.sapUiSizeCozy = getPixelValue("_sap_ui_table_BaseSizeCozy");
			mBaseSize.sapUiSizeCompact = getPixelValue("_sap_ui_table_BaseSizeCompact");
			mBaseSize.sapUiSizeCondensed = getPixelValue("_sap_ui_table_BaseSizeCondensed");
			iBaseBorderWidth = getPixelValue("_sap_ui_table_BaseBorderWidth");

			iRowHorizontalFrameSize = iBaseBorderWidth;
			mDefaultRowHeight.undefined = mBaseSize.undefined + iRowHorizontalFrameSize;
			mDefaultRowHeight.sapUiSizeCozy = mBaseSize.sapUiSizeCozy + iRowHorizontalFrameSize;
			mDefaultRowHeight.sapUiSizeCompact = mBaseSize.sapUiSizeCompact + iRowHorizontalFrameSize;
			mDefaultRowHeight.sapUiSizeCondensed = mBaseSize.sapUiSizeCondensed + iRowHorizontalFrameSize;

			mThemeParameters.navigationIcon = ThemeParameters.get("_sap_ui_table_NavigationIcon");
			mThemeParameters.deleteIcon = ThemeParameters.get("_sap_ui_table_DeleteIcon");
			mThemeParameters.resetIcon = ThemeParameters.get("_sap_ui_table_ResetIcon");
		}