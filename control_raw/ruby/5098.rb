def contextual_price_with_currency(rent_or_sale)
      contextual_price = self.contextual_price rent_or_sale

      if contextual_price.zero?
        return nil
      else
        return contextual_price.format(no_cents: true)
      end
      # return contextual_price.zero? ? nil : contextual_price.format(:no_cents => true)
    end