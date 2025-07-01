function (oData) {
				var FIRST_COLUMN = 0,
					SECOND_COLUMN = 1,
					THIRD_COLUMN = 2,
					ENTITIES_PER_COLUMN = 3,
					aHeaderControls = [[], [], []],
					oHeaderLayoutUtil = this._getHeaderLayoutUtil(),
					aHeaderBlocksInfo = [
						{creator: "_getApiReferenceBlock", exists: oData.bHasAPIReference},
						{creator: "_getDocumentationBlock", exists: oData.show.introLink},
						{creator: "_getUXGuidelinesBlock", exists: !!oData.uxGuidelinesLink},
						{creator: "_getExtendsBlock", exists: true},
						{creator: "_getApplicationComponentBlock", exists: true},
						{creator: "_getAvailableSinceBlock", exists: true},
						{creator: "_getCategoryBlock", exists: true},
						{creator: "_getContentDensityBlock", exists: true}
					],
					fnFillHeaderControlsStructure = function () {
						var iControlsAdded = 0,
							iIndexToAdd,
							fnGetIndexToAdd = function (iControlsAdded) {
								// determines the column(1st, 2nd or 3rd), the next entity data key-value should be added to.
								if (iControlsAdded <= ENTITIES_PER_COLUMN) {
									return FIRST_COLUMN;
								} else if (iControlsAdded <= ENTITIES_PER_COLUMN * 2) {
									return SECOND_COLUMN;
								}
								return THIRD_COLUMN;
							};

						aHeaderBlocksInfo.forEach(function (oHeaderBlockInfo) {
							var oControlBlock;
							if (oHeaderBlockInfo.exists) {
								oControlBlock = oHeaderLayoutUtil[oHeaderBlockInfo.creator].call(this, oData);
								iIndexToAdd = fnGetIndexToAdd(++iControlsAdded);
								aHeaderControls[iIndexToAdd].push(oControlBlock);
							}
						}, this);
					}.bind(this);

				// Creates the entity key-value controls
				// based on the existing entity key-value data,
				fnFillHeaderControlsStructure();

				// Wraps each column in a <code>sap.ui.layout.VerticalLayout</code>.
				aHeaderControls.forEach(function (aHeaderColumn, iIndex) {
					var oVL = this.byId("headerColumn" + iIndex);
					oVL.removeAllContent();

					if (aHeaderColumn.length > 0) {
						oVL.setVisible(true);
						aHeaderColumn.forEach(oVL.addContent, oVL);
					}
				}, this);
			}