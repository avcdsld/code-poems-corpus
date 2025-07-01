def fetch
      @source.gems.each do |gem|
        versions_for(gem).each do |versions|
          gem.platform = versions[1] if versions
          version = versions[0] if versions
          if gem.gemspec?
            gemfile = fetch_gemspec(gem, version)
            if gemfile
              Utils.configuration.mirror_gemspecs_directory
                   .add_file(gem.gemspec_filename(version), gemfile)
            end
          else
            gemfile = fetch_gem(gem, version)
            if gemfile
              Utils.configuration.mirror_gems_directory
                   .add_file(gem.filename(version), gemfile)
            end
          end
        end
      end
    end