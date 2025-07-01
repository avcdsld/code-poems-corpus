def tag!(tag, *args, &block)
      ele_id = nil

      # TODO: Move this logic to the tagset so that the tagset itself can validate + raise when invalid
      if @auto_validation && @tagset
        if !@tagset.tagset.has_key?(tag)
          raise InvalidXhtmlError, "no element `#{tag}' for #{tagset.doctype}"
        elsif args.last.respond_to?(:to_hash)
          attrs = args.last.to_hash

          if @tagset.forms.include?(tag) && attrs[:id]
            attrs[:name] ||= attrs[:id]
          end

          attrs.each do |k, v|
            atname = k.to_s.downcase.intern

            unless k =~ /:/ or @tagset.tagset[tag].include?(atname) or (@tagset == Markaby::HTML5 && atname.to_s =~ /^data-/)
              raise InvalidXhtmlError, "no attribute `#{k}' on #{tag} elements"
            end

            if atname == :id
              ele_id = v.to_s

              if @used_ids.has_key? ele_id
                raise InvalidXhtmlError, "id `#{ele_id}' already used (id's must be unique)."
              end
            end

            if AttrsBoolean.include? atname
              if v
                attrs[k] = atname.to_s
              else
                attrs.delete k
              end
            end
          end
        end
      end

      if block
        str = capture(&block)
        block = proc { text(str) }
      end

      f = fragment { @builder.tag!(tag, *args, &block) }
      @used_ids[ele_id] = f if ele_id
      f
    end