def get_with_user_credential(user_cred, resource = nil)
      logger.verbose('TokenRequest getting token with user credential ' \
                     "#{user_cred} and resource #{resource}.")
      oauth = if user_cred.is_a? UserIdentifier
                lambda do
                  fail UserCredentialError,
                       'UserIdentifier can only be used once there is a ' \
                       'matching token in the cache.'
                end
              end || -> {}
      request(user_cred.request_params.merge(RESOURCE => resource), &oauth)
    end