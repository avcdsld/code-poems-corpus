def format_key(key)
      key = key.to_s
      key = key.gsub('PayPal', 'Paypal')
      key = key.gsub('eBay',   'Ebay')
      key = key.gsub('EBay',   'Ebay')
      key.underscore.to_sym
    end