function (sId, oDoc, oEntity) {

			// convert docu
			var oData = this._convertEntityInfo(sId, oDoc),
				bShouldShowSamplesSection = false,
				iSamplesCount = 0;

			if (oEntity) {

				// show the description as intro text if the entity is not deprecated
				if (!oData.shortDescription && oEntity.description) {
					oData.shortDescription = oEntity.description;
				}

				// make intro text active if a documentation link is set
				if (oEntity.docuLink) {
					oData.show.introLink = true;
					oData.docuLink = oEntity.docuLink;
				}

				bShouldShowSamplesSection = oEntity.samples.length > 0;
				iSamplesCount = oEntity.samples.length;
			}

			// apply entity related stuff
			oData.show.samples = bShouldShowSamplesSection;
			oData.count.samples = iSamplesCount;

			// done
			return oData;
		}