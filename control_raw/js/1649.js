function handlePermissions(options) {
            if (permissions.parseContext(options.context).internal) {
                return Promise.resolve(options);
            }

            return canThis(options.context).add.notification().then(() => {
                return options;
            }, () => {
                return Promise.reject(new common.errors.NoPermissionError({
                    message: common.i18n.t('errors.api.notifications.noPermissionToAddNotif')
                }));
            });
        }