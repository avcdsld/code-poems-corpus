function(message) {
			this._clickToDisMiss = false;
			this._init();
			this.progressMessage = message;

			var pageLoader = getPageLoader();
			if (pageLoader) {

				var step = pageLoader.getStep();
				if(step) {
					if (typeof message === "object") {
						step.message = message.message;
						step.detailedMessage = message.detailedMessage;
					} else {
						step.message = message;
						step.detailedMessage = "";
					}
					pageLoader.update();
					return;
				}
			}

			var node = lib.node(this.progressDomId);
			lib.empty(node);
			node.appendChild(document.createTextNode(message));

			var container = lib.node(this.notificationContainerDomId);
			container.classList.remove("notificationHide"); //$NON-NLS-0$
			if (message && message.length > 0) {
				container.classList.add("progressNormal"); //$NON-NLS-0$
				container.classList.add("notificationShow"); //$NON-NLS-0$
			} else if(this._progressMonitors && this._progressMonitors.length > 0){
				return this._renderOngoingMonitors();
			}else{
				container.classList.remove("notificationShow"); //$NON-NLS-0$
				container.classList.add("notificationHide"); //$NON-NLS-0$
			}
		}