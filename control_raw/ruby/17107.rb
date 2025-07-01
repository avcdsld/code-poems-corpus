def variants
      return @_variants if @_variants

      @_variants = self.class.ancestors.select {|c| c.to_s =~ /^Jpmobile/ && c.to_s !~ /Emoticon/ }.map do |klass|
        klass = klass.to_s.
                  gsub(/Jpmobile::/, '').
                  gsub(/AbstractMobile::/, '').
                  gsub(/Mobile::SmartPhone/, 'smart_phone').
                  gsub(/Mobile::Tablet/, 'tablet').
                  gsub(/::/, '_').
                  gsub(/([A-Z]+)([A-Z][a-z])/, '\1_\2').
                  gsub(/([a-z\d])([A-Z])/, '\1_\2').
                  downcase
        (klass =~ /abstract/) ? 'mobile' : klass
      end

      if @_variants.include?('tablet')
        @_variants = @_variants.reject {|v| v == 'mobile' }.map {|v| v.gsub(/mobile_/, 'tablet_') }
      elsif @_variants.include?('smart_phone')
        @_variants = @_variants.reject {|v| v == 'mobile' }.map {|v| v.gsub(/mobile_/, 'smart_phone_') }
      end

      @_variants || []
    end