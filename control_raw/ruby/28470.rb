def save_config
      botpart_config = Hash[@config.to_a - $bot[:config].to_a]

      unless botpart_config.empty?
        File.open @botpart_config_path, 'w' do |f|
          f.write botpart_config.to_yaml
        end
      end
    end