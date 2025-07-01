def generate
      if level.number == 1
        FileUtils.mkdir_p(level.player_path) unless File.exists? level.player_path
        FileUtils.cp(templates_path + '/player.rb', level.player_path)
      end
      
      File.open(level.player_path + '/README', 'w') do |f|
        f.write read_template(templates_path + '/README.erb')
      end
    end