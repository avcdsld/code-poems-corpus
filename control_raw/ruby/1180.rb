def fetch_github_token
      env_var = @options[:token].presence || ENV["CHANGELOG_GITHUB_TOKEN"]

      Helper.log.warn NO_TOKEN_PROVIDED unless env_var

      env_var
    end