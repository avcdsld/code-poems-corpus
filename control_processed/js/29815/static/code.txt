function(data) {
				rebaseCallback(data).then(function() {
					dispatchModelEventOn({type: "modelChanged", action: "rebase", item: data.items}); //$NON-NLS-1$ //$NON-NLS-0$
				}, function() {
					dispatchModelEventOn({type: "modelChanged", action: "rebase", item: data.items, failed: true}); //$NON-NLS-1$ //$NON-NLS-0$
				});
			}