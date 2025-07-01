def command(cmd, explicit)
      return false unless check_pipe_exist(explicit)

      Timeout.timeout 5 do
        File.open @pipe, 'w' do |p|
          p.puts cmd
        end
      end
      true
    rescue Timeout::Error
      communication_error! 'no response'
    end