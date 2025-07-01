def new_column(type, label=nil, id =nil, role=nil, pattern=nil)
      column = { :type => type, :label => label, :id => id, :role => role, :pattern => pattern }.reject { |key, value| value.nil? }
      @cols << column
    end