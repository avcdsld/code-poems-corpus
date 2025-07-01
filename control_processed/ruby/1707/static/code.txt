def virtual_mfa_devices(options = {})
      batches = Enumerator.new do |y|
        resp = @client.list_virtual_mfa_devices(options)
        resp.each_page do |page|
          batch = []
          page.data.virtual_mfa_devices.each do |v|
            batch << VirtualMfaDevice.new(
              serial_number: v.serial_number,
              data: v,
              client: @client
            )
          end
          y.yield(batch)
        end
      end
      VirtualMfaDevice::Collection.new(batches)
    end