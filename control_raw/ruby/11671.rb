def create_snapshot(name)
      raise Fission::Error,"VM #{@name} does not exist" unless self.exists?

      command = "#{vmrun_cmd} snapshot #{vmx_path.shellescape} \"#{name}\" 2>&1"
      output = `#{command}`

      response = Fission::Response.new :code => $?.exitstatus
      response.output = output unless response.successful?

      response
    end