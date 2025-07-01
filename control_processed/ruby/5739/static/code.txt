def strip_tags(string)
      if defined?(Loofah)
        # Instead of strip_tags we will use Loofah to strip tags from now on
        Loofah.fragment(string).text(encode_special_chars: false)
      else
        helpers.strip_tags(string)
      end
    end