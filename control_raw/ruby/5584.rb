def parse_tag(text)
      match = text.scan(/%([-:\w]+)([-:\w.#\@]*)(.+)?/)[0]
      raise SyntaxError.new(Error.message(:invalid_tag, text)) unless match

      tag_name, attributes, rest = match

      if !attributes.empty? && (attributes =~ /[.#](\.|#|\z)/)
        raise SyntaxError.new(Error.message(:illegal_element))
      end

      new_attributes_hash = old_attributes_hash = last_line = nil
      object_ref = :nil
      attributes_hashes = {}
      while rest && !rest.empty?
        case rest[0]
        when ?{
          break if old_attributes_hash
          old_attributes_hash, rest, last_line = parse_old_attributes(rest)
          attributes_hashes[:old] = old_attributes_hash
        when ?(
          break if new_attributes_hash
          new_attributes_hash, rest, last_line = parse_new_attributes(rest)
          attributes_hashes[:new] = new_attributes_hash
        when ?[
          break unless object_ref == :nil
          object_ref, rest = balance(rest, ?[, ?])
        else; break
        end
      end

      if rest && !rest.empty?
        nuke_whitespace, action, value = rest.scan(/(<>|><|[><])?([=\/\~&!])?(.*)?/)[0]
        if nuke_whitespace
          nuke_outer_whitespace = nuke_whitespace.include? '>'
          nuke_inner_whitespace = nuke_whitespace.include? '<'
        end
      end

      if @options.remove_whitespace
        nuke_outer_whitespace = true
        nuke_inner_whitespace = true
      end

      if value.nil?
        value = ''
      else
        value.strip!
      end
      [tag_name, attributes, attributes_hashes, object_ref, nuke_outer_whitespace,
       nuke_inner_whitespace, action, value, last_line || @line.index + 1]
    end