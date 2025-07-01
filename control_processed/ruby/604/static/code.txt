def prepare_list
      UI.message("Fetching certificates and profiles...")
      cert_type = Match.cert_type_sym(type)

      prov_types = []
      prov_types = [:development] if cert_type == :development
      prov_types = [:appstore, :adhoc] if cert_type == :distribution
      prov_types = [:enterprise] if cert_type == :enterprise

      Spaceship.login(params[:username])
      Spaceship.select_team

      if Spaceship.client.in_house? && (type == "distribution" || type == "enterprise")
        UI.error("---")
        UI.error("⚠️ Warning: This seems to be an Enterprise account!")
        UI.error("By nuking your account's distribution, all your apps deployed via ad-hoc will stop working!") if type == "distribution"
        UI.error("By nuking your account's enterprise, all your in-house apps will stop working!") if type == "enterprise"
        UI.error("---")

        UI.user_error!("Enterprise account nuke cancelled") unless UI.confirm("Do you really want to nuke your Enterprise account?")
      end

      self.certs = certificate_type(cert_type).all
      self.profiles = []
      prov_types.each do |prov_type|
        self.profiles += profile_type(prov_type).all
      end

      certs = Dir[File.join(self.storage.working_directory, "**", cert_type.to_s, "*.cer")]
      keys = Dir[File.join(self.storage.working_directory, "**", cert_type.to_s, "*.p12")]
      profiles = []
      prov_types.each do |prov_type|
        profiles += Dir[File.join(self.storage.working_directory, "**", prov_type.to_s, "*.mobileprovision")]
      end

      self.files = certs + keys + profiles
    end