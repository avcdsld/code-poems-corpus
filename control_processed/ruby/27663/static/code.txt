def perform
        begin
          required_options :service_id
          @name = options["service_id"]
          @metadata = VCAP.symbolize_keys(options["metadata"])
          @logger.info("Launch job: #{self.class} for #{name} with metadata: #{@metadata}")

          @snapshot_id = new_snapshot_id
          lock = create_lock

          @snapshot_files = []
          lock.lock do
            quota = @config["snapshot_quota"]
            if quota
              current = service_snapshots_count(name)
              @logger.debug("Current snapshots count for #{name}: #{current}, max: #{quota}")
              raise ServiceError.new(ServiceError::OVER_QUOTA, name, current, quota) if current >= quota
            end

            snapshot = execute
            snapshot = VCAP.symbolize_keys snapshot
            snapshot[:manifest] ||= {}
            snapshot[:manifest].merge! @metadata
            @logger.info("Results of create snapshot: #{snapshot.inspect}")

            # pack snapshot_file into package
            dump_path = get_dump_path(name, snapshot_id)
            FileUtils.mkdir_p(dump_path)
            package_file = "#{snapshot_id}.zip"

            package = Package.new(File.join(dump_path, package_file))
            package.manifest = snapshot[:manifest]
            files = Array(snapshot[:files])
            raise "No snapshot file to package." if files.empty?
            files.each do |f|
              full_path = File.join(dump_path, f)
              @snapshot_files << full_path
              package.add_files full_path
            end
            package.pack(dump_path)
            @logger.info("Package snapshot file: #{File.join(dump_path, package_file)}")

            # update snapshot metadata for package file
            snapshot.delete(:files)
            snapshot[:file] = package_file
            snapshot[:date] = fmt_time
            # add default service name
            snapshot[:name] = "Snapshot #{snapshot[:date]}"

            save_snapshot(name, snapshot)

            completed(Yajl::Encoder.encode(filter_keys(snapshot)))
            @logger.info("Complete job: #{self.class} for #{name}")
          end
        rescue => e
          cleanup(name, snapshot_id)
          handle_error(e)
        ensure
          set_status({:complete_time => Time.now.to_s})
          @snapshot_files.each{|f| File.delete(f) if File.exists? f} if @snapshot_files
        end
      end