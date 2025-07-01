def linkify(*args)
      if args.first.is_a?(String)
        case args.first
        when %r{://}, /^mailto:/
          link_url(args[0], args[1], {:target => '_parent'}.merge(args[2] || {}))
        when /^include:file:(\S+)/
          file = $1
          relpath = File.relative_path(Dir.pwd, File.expand_path(file))
          if relpath =~ /^\.\./
            log.warn "Cannot include file from path `#{file}'"
            ""
          elsif File.file?(file)
            link_include_file(file)
          else
            log.warn "Cannot find file at `#{file}' for inclusion"
            ""
          end
        when /^include:(\S+)/
          path = $1
          obj = YARD::Registry.resolve(object.namespace, path)
          if obj
            link_include_object(obj)
          else
            log.warn "Cannot find object at `#{path}' for inclusion"
            ""
          end
        when /^render:(\S+)/
          path = $1
          obj = YARD::Registry.resolve(object, path)
          if obj
            opts = options.dup
            opts.delete(:serializer)
            obj.format(opts)
          else
            ''
          end
        when /^file:(\S+?)(?:#(\S+))?$/
          link_file($1, args[1] ? args[1] : nil, $2)
        else
          link_object(*args)
        end
      else
        link_object(*args)
      end
    end