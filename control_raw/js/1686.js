function doQuery(options) {
            return models.User.changePassword(
                options.data.password[0],
                _.omit(options, ['data'])
            ).then(() => {
                return Promise.resolve({
                    password: [{message: common.i18n.t('notices.api.users.pwdChangedSuccessfully')}]
                });
            });
        }