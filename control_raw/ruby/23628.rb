def called_from
      location = caller.detect('unknown:0') do |line|
        line.match(/\/liquid(-|\/)ext/).nil?
      end
      file, line, _ = location.split(':')
      { :file => file, :line => line }
    end