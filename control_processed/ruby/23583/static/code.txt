def destroy_sandbox
        if File.directory?(Strainer.sandbox_path)
          Strainer.ui.debug "  Destroying sandbox at '#{Strainer.sandbox_path}'"
          FileUtils.rm_rf(Strainer.sandbox_path)
        else
          Strainer.ui.debug "  Sandbox does not exist... skipping"
        end
      end