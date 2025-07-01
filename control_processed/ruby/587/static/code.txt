def run
      FastlaneCore::PrintTable.print_values(config: Sigh.config,
                                         hide_keys: [:output_path],
                                             title: "Summary for sigh #{Fastlane::VERSION}")

      UI.message("Starting login with user '#{Sigh.config[:username]}'")
      Spaceship.login(Sigh.config[:username], nil)
      Spaceship.select_team
      UI.message("Successfully logged in")

      profiles = [] if Sigh.config[:skip_fetch_profiles]
      profiles ||= fetch_profiles # download the profile if it's there

      if profiles.count > 0
        UI.success("Found #{profiles.count} matching profile(s)")
        profile = profiles.first

        if Sigh.config[:force]
          # Recreating the profile ensures it has all of the requested properties (cert, name, etc.)
          UI.important("Recreating the profile")
          profile.delete!
          profile = create_profile!
        end
      else
        UI.user_error!("No matching provisioning profile found and can not create a new one because you enabled `readonly`") if Sigh.config[:readonly]
        UI.important("No existing profiles found, that match the certificates you have installed locally! Creating a new provisioning profile for you")
        ensure_app_exists!
        profile = create_profile!
      end

      UI.user_error!("Something went wrong fetching the latest profile") unless profile

      if profile_type == Spaceship.provisioning_profile.in_house
        ENV["SIGH_PROFILE_ENTERPRISE"] = "1"
      else
        ENV.delete("SIGH_PROFILE_ENTERPRISE")
      end

      return download_profile(profile)
    end