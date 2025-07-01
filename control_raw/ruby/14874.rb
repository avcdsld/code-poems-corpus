def close_io
      [@write_io, @read_io].each do |io|
        begin
          io.close unless io.closed?
        rescue IOError
          raise unless RUBY_ENGINE == 'jruby'
        end
      end
    end