function handlePermissions(options) {
            return canThis(options.context).destroy.notification().then(() => {
                return options;
            }, () => {
                return Promise.reject(new common.errors.NoPermissionError({
                    message: common.i18n.t('errors.api.notifications.noPermissionToDestroyNotif')
                }));
            });
        }