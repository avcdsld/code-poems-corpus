def change_dylib_id(new_id, _options = {})
      raise ArgumentError, "new ID must be a String" unless new_id.is_a?(String)
      return unless dylib?

      old_lc = command(:LC_ID_DYLIB).first
      raise DylibIdMissingError unless old_lc

      new_lc = LoadCommands::LoadCommand.create(:LC_ID_DYLIB, new_id,
                                                old_lc.timestamp,
                                                old_lc.current_version,
                                                old_lc.compatibility_version)

      replace_command(old_lc, new_lc)
    end