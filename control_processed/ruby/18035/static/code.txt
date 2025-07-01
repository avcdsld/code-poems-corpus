def install_file(source, dest, is_dir=false)
      if File.exists?(dest)
        print "#{dest} already exists. Overwrite it? (yes/no) "
        return unless ['y', 'yes', 'ok'].include? gets.chomp.downcase
      end
      is_dir ? FileUtils.cp_r(source, dest) : FileUtils.cp(source, dest)
      puts "installed #{dest}" unless ENV['RACK_ENV'] == 'test'
    end