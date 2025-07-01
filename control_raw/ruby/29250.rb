def seed_from_dump id
      target_path = File.expand_path("../../fixtures/trunk-#{id}.dump", __FILE__)
      raise "Dump #{id} could not be found." unless File.exists? target_path
      
      puts "Restoring #{ENV['RACK_ENV']} database from #{target_path}"
      
      # Ensure we're starting from a clean DB.
      system "dropdb trunk_cocoapods_org_test"
      system "createdb trunk_cocoapods_org_test"
      
      # Restore the DB.
      command = "pg_restore --no-privileges --clean --no-acl --no-owner -h localhost -d trunk_cocoapods_org_test #{target_path}"
      puts "Executing:"
      puts command
      puts
      result = system command
      if result
        puts "Database #{ENV['RACK_ENV']} restored from #{target_path}"
      else
        warn "Database #{ENV['RACK_ENV']} restored from #{target_path} with some errors."
        # exit 1
      end
    end