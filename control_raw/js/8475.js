function(mOptions) {
			mOptions = mOptions || {};
			if (typeof mOptions !== "object") {
				throw new Error("Parameter object isn't a valid object");
			}

			// Reset all parameters to default
			this.mHarFileContent = null;
			this.aRequests = [];
			this.sFilename = "";
			this.bIsRecording = false;
			this.bIsPaused = false;
			this.bIsDownloadDisabled = false;
			if (this.oSinonXhr) {
				this.oSinonXhr.filters = this.aSinonFilters;
				this.aSinonFilters = [];
				this.oSinonXhr.restore();
				this.oSinonXhr = null;
			}

			// Restore native XHR functions if they were overwritten.
			for (var sFunctionName in this.mXhrNativeFunctions) {
				if (this.mXhrNativeFunctions.hasOwnProperty(sFunctionName)) {
					window.XMLHttpRequest.prototype[sFunctionName] = this.mXhrNativeFunctions[sFunctionName];
				}
			}
			this.mXhrNativeFunctions = {};

			// Set options to provided values or to default
			this.bIsDownloadDisabled = mOptions.disableDownload === true;
			this.bPromptForDownloadFilename = mOptions.promptForDownloadFilename === true;

			if (mOptions.delay) {
				if (mOptions.delay === true) {
					this.mDelaySettings = {}; // Use delay of recording
				} else {
					this.mDelaySettings = mOptions.delay;
				}
			} else {
				this.mDelaySettings = { max: 0 }; // default: no delay
			}
			if (mOptions.entriesUrlFilter) {
				if (Array.isArray(mOptions.entriesUrlFilter)) {
					this.aEntriesUrlFilter = mOptions.entriesUrlFilter;
				} else {
					this.aEntriesUrlFilter = [mOptions.entriesUrlFilter];
				}
			} else {
				this.aEntriesUrlFilter = [new RegExp(".*")]; // default: no filtering
			}
			if (mOptions.entriesUrlReplace) {
				if (Array.isArray(mOptions.entriesUrlReplace)) {
					this.aEntriesUrlReplace = mOptions.entriesUrlReplace;
				} else {
					this.aEntriesUrlReplace = [mOptions.entriesUrlReplace];
				}
			} else {
				this.aEntriesUrlReplace = [];
			}

			if (mOptions.customGroupNameCallback && typeof mOptions.customGroupNameCallback === "function") {
				this.fnCustomGroupNameCallback = mOptions.customGroupNameCallback;
			} else {
				this.fnCustomGroupNameCallback = function() { return false; }; // default: Empty Callback function used
			}
		}