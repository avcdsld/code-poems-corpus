def execute
      process_output(execute!)

    rescue ::OpenSSL::Cipher::CipherError => e
      { reason:    'Invalid key provided',
        exception: e }

    rescue Sym::Errors::Error => e
      { reason:    e.class.name.gsub(/.*::/, '').underscore.humanize.downcase,
        exception: e }

    rescue TypeError => e
      if e.message =~ /marshal/m
        { reason:    'Corrupt source data or invalid/corrupt key provided',
          exception: e }
      else
        { exception: e }
      end

    rescue StandardError => e
      { exception: e }
    end