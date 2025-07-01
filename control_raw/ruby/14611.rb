def target_name
      # cmdkey command is used for accessing windows credential manager.
      # Multiple credentials get created in windows credential manager for a single Azure account in xplat-cli
      # One of them is for common tanent id, which can't be used
      # Others end with --0-x,--1-x,--2-x etc, where x represents the total no. of credentails across which the token is divided
      # The one ending with --0-x has the complete accessToken in the credentialBlob.
      # Refresh Token is split across both credentials (ending with --0-x and --1-x).
      # Xplat splits the credentials based on the number of bytes of the tokens.
      # Hence the access token is always found in the one which start with --0-
      # So selecting the credential on the basis of --0-
      xplat_creds_cmd = Mixlib::ShellOut.new('cmdkey /list | findstr AzureXplatCli | findstr \--0- | findstr -v common')
      result = xplat_creds_cmd.run_command
      target_names = []

      if result.stdout.empty?
        Chef::Log.debug("Unable to find a credential with --0- and falling back to looking for any credential.")
        xplat_creds_cmd = Mixlib::ShellOut.new("cmdkey /list | findstr AzureXplatCli | findstr -v common")
        result = xplat_creds_cmd.run_command

        if result.stdout.empty?
          raise "Azure Credentials not found. Please run xplat's 'azure login' command"
        else
          target_names = result.stdout.split("\n")
        end
      else
        target_names = result.stdout.split("\n")
      end

      # If "azure login" is run for multiple users, there will be multiple credentials
      # Picking up the latest logged in user's credentials
      latest_target = latest_credential_target target_names
      latest_target
    end