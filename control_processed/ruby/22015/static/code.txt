def migrate!
      @semaphore.synchronize do
        return unless @active

        networks = @core.config.networks
        (@checkpoint - networks).each { |network| disconnect_from network }
        (networks - @checkpoint).each { |network| connect_to      network }
        @checkpoint = networks
      end
    end