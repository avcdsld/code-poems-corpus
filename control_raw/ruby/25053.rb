def respond_to?(method)
    if @collections.include?(method.to_s)
      return true
    # Adds
    elsif method.to_s =~ /^AddTo(.*)/
      type = $1
      if @collections.include?(type)
        return true
      else
        super
      end
    # Function Imports
    elsif @function_imports.include?(method.to_s)
      return true
    else
      super
    end
  end