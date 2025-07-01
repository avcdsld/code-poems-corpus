def access_token=(token)
      token, scope = token.sub(/^bearer\s+/i, '').split(' ', 2)
      if scope
        warn "[DEPRECATION] (gocardless-ruby) merchant_id is now a separate " +
             "attribute, the manage_merchant scope should no longer be " +
             "included in the 'token' attribute. See http://git.io/G9y37Q " +
             "for more info."
      else
        scope = ''
      end

      @access_token = OAuth2::AccessToken.new(@oauth_client, token)
      @access_token.params['scope'] = scope

      set_merchant_id_from_scope(scope) unless @merchant_id
    end