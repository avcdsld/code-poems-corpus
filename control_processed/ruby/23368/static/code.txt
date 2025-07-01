def view
      pager = ENV['PAGER'] || 'less'
      execute_external_command do
        unless in_zip?
          system %Q[#{pager} "#{current_item.path}"]
        else
          begin
            tmpdir, tmpfile_name = nil
            Zip::File.open(current_zip) do |zip|
              tmpdir = Dir.mktmpdir
              FileUtils.mkdir_p File.join(tmpdir, File.dirname(current_item.name))
              tmpfile_name = File.join(tmpdir, current_item.name)
              File.open(tmpfile_name, 'w') {|f| f.puts zip.file.read(current_item.name)}
            end
            system %Q[#{pager} "#{tmpfile_name}"]
          ensure
            FileUtils.remove_entry_secure tmpdir if tmpdir
          end
        end
      end
    end