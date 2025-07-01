def login(locale: DEFAULT_LOCALE)
      if user = self.class.login(self.user_id, self.password, locale: locale)
        self.name = user.name
        self
      end
    end