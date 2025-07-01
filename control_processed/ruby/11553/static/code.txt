def add_tag(tag)
      if @counters[:attributes][:tag] >= Mailgun::Chains::MAX_TAGS
        fail Mailgun::ParameterError, 'Too many tags added to message.', tag
      end
      set_multi_complex('o:tag', tag)
      @counters[:attributes][:tag] += 1
    end