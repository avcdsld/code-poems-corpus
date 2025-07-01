def copy(source, target, options={})
      source = source.sub(/^\//, '')
      target = target.sub(/^\//, '')
      target << File.basename(source) if target.ends_with?('/')
      begin
        parse_metadata(post('fileops', 'copy', :from_path => Dropbox.check_path(source), :to_path => Dropbox.check_path(target), :root => root(options), :ssl => @ssl)).to_struct_recursively
      rescue UnsuccessfulResponseError => error
        raise FileNotFoundError.new(source) if error.response.kind_of?(Net::HTTPNotFound)
        raise FileExistsError.new(target) if error.response.kind_of?(Net::HTTPForbidden)
        raise error
      end
    end