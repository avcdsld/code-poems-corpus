def brainstem_present(name, options = {}, &block)
      Brainstem.presenter_collection(options[:namespace]).presenting(name, options.reverse_merge(:params => params), &block)
    end