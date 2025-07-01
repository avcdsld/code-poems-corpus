def alias_color(alias_name, *colors)
      validate(*colors)

      if !(alias_name.to_s =~ /^[\w]+$/)
        fail InvalidAliasNameError, "Invalid alias name `#{alias_name}`"
      elsif ANSI::ATTRIBUTES[alias_name]
        fail InvalidAliasNameError,
             "Cannot alias standard color `#{alias_name}`"
      end

      ALIASES[alias_name.to_sym] = colors.map(&ANSI::ATTRIBUTES.method(:[]))
      colors
    end