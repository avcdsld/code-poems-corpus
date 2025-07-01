def profit_and_loss_amount
      raise 'profit_and_loss does not start with the expected currency' unless profit_and_loss.start_with? currency

      profit_and_loss[currency.length..-1].delete(',').to_f
    end