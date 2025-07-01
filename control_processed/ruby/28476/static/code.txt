def weburl(locale: nil, domain: DEFAULT_DOMAIN)
      locale ||= self.lc || DEFAULT_LOCALE

      if self.code && prefix = LOCALE_WEBURL_PREFIXES[locale]
        path = "#{prefix}/#{self.code}"
        "https://#{locale}.#{domain}/#{path}"
      end
    end