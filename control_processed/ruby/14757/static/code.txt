def find_applications_by_app_name(app_name)
      pids = []

      begin
        x = `ps auxw | grep -v grep | awk '{print $2, $11, $12}' | grep #{app_name}`
        if x && x.chomp!
          processes = x.split(/\n/).compact
          processes = processes.delete_if do |p|
            _pid, name, add = p.split(/\s/)
            # We want to make sure that the first part of the process name matches
            # so that app_name matches app_name_22

            app_name != name[0..(app_name.length - 1)] and not add.include?(app_name)
          end
          pids = processes.map { |p| p.split(/\s/)[0].to_i }
        end
        rescue ::Exception
      end

      pids.map do |f|
        app = Application.new(self, {}, PidMem.existing(f))
        setup_app(app)
        app
      end
    end