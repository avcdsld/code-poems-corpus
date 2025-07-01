def add_error(attribute, message)
    @errors[attribute] ||= []
    @errors[attribute] = @errors[attribute] << message unless @errors[attribute].include? message
    @errors
  end