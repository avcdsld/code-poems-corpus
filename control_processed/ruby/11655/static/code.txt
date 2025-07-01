def format_code(text)
      simple_format( truncate( Sanitize.clean(markdown(text)).html_safe, escape: false, length: 300, separator: ' ', omission: ' …' ))
    end