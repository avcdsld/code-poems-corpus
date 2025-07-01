def save
      if @in_jss
        raise JSS::UnsupportedError, 'Updating this object in the JSS is currently not supported by ruby-jss' unless updatable?
        update
      else
        raise JSS::UnsupportedError, 'Creating this object in the JSS is currently not supported by ruby-jss' unless creatable?
        create
      end
    end