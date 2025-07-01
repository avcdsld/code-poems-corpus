def update_signature!
      result = Overcommit::Utils.execute(
        %w[git config --local] + [signature_config_key, signature]
      )

      unless result.success?
        raise Overcommit::Exceptions::GitConfigError,
              "Unable to write to local repo git config: #{result.stderr}"
      end
    end