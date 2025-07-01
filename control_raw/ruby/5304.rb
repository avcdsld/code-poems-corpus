def join(uri)
      if !uri.respond_to?(:to_str)
        raise TypeError, "Can't convert #{uri.class} into String."
      end
      if !uri.kind_of?(URI)
        # Otherwise, convert to a String, then parse.
        uri = URI.parse(uri.to_str)
      end
      if uri.to_s.empty?
        return self.dup
      end

      joined_scheme = nil
      joined_user = nil
      joined_password = nil
      joined_host = nil
      joined_port = nil
      joined_path = nil
      joined_query = nil
      joined_fragment = nil

      # Section 5.2.2 of RFC 3986
      if uri.scheme != nil
        joined_scheme = uri.scheme
        joined_user = uri.user
        joined_password = uri.password
        joined_host = uri.host
        joined_port = uri.port
        joined_path = URI.normalize_path(uri.path)
        joined_query = uri.query
      else
        if uri.authority != nil
          joined_user = uri.user
          joined_password = uri.password
          joined_host = uri.host
          joined_port = uri.port
          joined_path = URI.normalize_path(uri.path)
          joined_query = uri.query
        else
          if uri.path == nil || uri.path.empty?
            joined_path = self.path
            if uri.query != nil
              joined_query = uri.query
            else
              joined_query = self.query
            end
          else
            if uri.path[0..0] == SLASH
              joined_path = URI.normalize_path(uri.path)
            else
              base_path = self.path.dup
              base_path = EMPTY_STR if base_path == nil
              base_path = URI.normalize_path(base_path)

              # Section 5.2.3 of RFC 3986
              #
              # Removes the right-most path segment from the base path.
              if base_path =~ /\//
                base_path.sub!(/\/[^\/]+$/, SLASH)
              else
                base_path = EMPTY_STR
              end

              # If the base path is empty and an authority segment has been
              # defined, use a base path of SLASH
              if base_path.empty? && self.authority != nil
                base_path = SLASH
              end

              joined_path = URI.normalize_path(base_path + uri.path)
            end
            joined_query = uri.query
          end
          joined_user = self.user
          joined_password = self.password
          joined_host = self.host
          joined_port = self.port
        end
        joined_scheme = self.scheme
      end
      joined_fragment = uri.fragment

      return self.class.new(
        :scheme => joined_scheme,
        :user => joined_user,
        :password => joined_password,
        :host => joined_host,
        :port => joined_port,
        :path => joined_path,
        :query => joined_query,
        :fragment => joined_fragment
      )
    end