function () {
				this._oComponent = sap.ui.component("sap.uxap");
				if (!this._oComponent) {
					this._oComponent = sap.ui.component({
						name: this.getName(),
						url: this.getUrl(),
						componentData: {            //forward configuration to underlying component
							jsonConfigurationURL: this.getJsonConfigurationURL(),
							mode: this.getMode()
						}
					});

					this.setComponent(this._oComponent, true);
				}

				// call the parent onBeforeRendering
				if (ComponentContainer.prototype.onBeforeRendering) {
					ComponentContainer.prototype.onBeforeRendering.call(this);
				}
			}