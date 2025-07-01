def scm(force = false)
      return @_scm if @_scm && !force

      case config[:scm]
      when :git
        @_scm = Release::Scm::Git.new(path: source_path)
      when :fixed
        @_scm = Release::Scm::Fixed.new
      else
        raise "Unknown SCM #{options[:scm].inspect}"
      end
    end