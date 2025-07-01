def compare_settings(produced, expected, params)
      it 'should match build settings' do
        # Find faulty settings in different categories
        missing_settings    = expected.keys.reject { |k| produced.key?(k) }
        unexpected_settings = produced.keys.reject { |k| expected.key?(k) }
        wrong_settings      = (expected.keys - missing_settings).select do |k|
          produced_setting = produced[k]
          produced_setting = produced_setting.join(' ') if produced_setting.respond_to? :join
          produced_setting != expected[k]
        end

        # Build pretty description for what is going on
        description = []
        description << "Doesn't match build settings for \e[1m#{params}\e[0m"

        if wrong_settings.count > 0
          description << 'Wrong build settings:'
          description += wrong_settings.map { |s| "* #{s.to_s.yellow} is #{produced[s].to_s.red}, but should be #{expected[s].to_s.green}" }
          description << ''
        end

        if missing_settings.count > 0
          description << 'Missing build settings:'
          description << missing_settings.map { |s| "* #{s.to_s.red} (#{expected[s]})" }
          description << ''
        end

        if unexpected_settings.count > 0
          description << 'Unexpected additional build settings:'
          description += unexpected_settings.map { |s| "* #{s.to_s.green} (#{produced[s]})" }
          description << ''
        end

        # Expect
        faulty_settings = missing_settings + unexpected_settings + wrong_settings
        faulty_settings.should.satisfy(description * "\n") do
          faulty_settings.length == 0
        end
      end
    end