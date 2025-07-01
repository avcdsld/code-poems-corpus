def icon_position=(position)
      raise ArgumentError.new("icon_position must be one of #{ICON_POSITIONS}") unless ICON_POSITIONS.include? position

      @icon_position = position

      case @icon_position
        when :top, :bottom
          @contents.instance_variable_set :@type, :fixed_columns
          @contents.instance_variable_set :@num_columns, 1
        when :left, :right
          @contents.instance_variable_set :@type, :fixed_rows
          @contents.instance_variable_set :@num_rows, 1
      end

      self.icon = @icon.image if @icon.image # Force the icon into the correct position.

      position
    end