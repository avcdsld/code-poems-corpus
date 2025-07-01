def method
      @method ||= begin
        request_method = @env[Merb::Const::REQUEST_METHOD].downcase.to_sym
        case request_method
        when :get, :head, :put, :delete, :options
          request_method
        when :post
          m = nil
          self.class.http_method_overrides.each do |o|
            m ||= o.call(self); break if m
          end
          m.downcase! if m
          METHODS.include?(m) ? m.to_sym : :post
        else
          raise "Unknown REQUEST_METHOD: #{@env[Merb::Const::REQUEST_METHOD]}"
        end
      end
    end