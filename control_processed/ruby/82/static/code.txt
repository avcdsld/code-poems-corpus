def _wrapper_enabled?
        return false unless request.has_content_type?

        ref = request.content_mime_type.ref
        _wrapper_formats.include?(ref) && _wrapper_key && !request.parameters.key?(_wrapper_key)
      end