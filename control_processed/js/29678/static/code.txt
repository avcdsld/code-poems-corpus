function(data) {
				var item = data.items;
				var dialog = new ResetPasswordDialog.ResetPasswordDialog({
					user: item,
					registry : serviceRegistry
				});
				dialog.show();
				
			}