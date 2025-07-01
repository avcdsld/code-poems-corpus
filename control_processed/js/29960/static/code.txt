function (project) {
			if (project) {
				this._projectClient.getProjectLaunchConfigurations(project).then(function(launchConfigurations){
					if (project !== this._project) return;
					this._setLaunchConfigurations(launchConfigurations);
				}.bind(this));
			} else {
				this._setLaunchConfigurations(null);
			}
		}