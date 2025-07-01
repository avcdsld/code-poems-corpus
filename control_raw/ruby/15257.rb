def import
      color_aliases = env['PASTEL_COLORS_ALIASES']
      return unless color_aliases
      color_aliases.split(',').each do |color_alias|
        new_color, old_colors = color_alias.split('=')
        if !new_color || !old_colors
          output.puts "Bad color mapping `#{color_alias}`"
        else
          color.alias_color(new_color.to_sym,
                            *old_colors.split('.').map(&:to_sym))
        end
      end
    end