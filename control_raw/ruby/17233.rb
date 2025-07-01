def redeem!(account_code, currency = nil)
      redemption = redeem(account_code, currency)
      raise Invalid.new(self) unless redemption && redemption.persisted?
      redemption
    end