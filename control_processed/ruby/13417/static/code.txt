def _setup(action)
        @cipher ||= OpenSSL::Cipher.new(@options[:cipher]) 
        # Toggles encryption mode
        @cipher.send(action)
        @cipher.padding = @options[:padding]
        @cipher.key = @key.unpack('a2'*32).map{|x| x.hex}.pack('c'*32)
      end