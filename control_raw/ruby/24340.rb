def re_raise_error(body)
      error = body.fetch(:message, nil)
      case body.fetch(:glimrerrorcode, nil)
      when 511 # FeeLiability not found for FeeLiabilityID
        raise FeeLiabilityNotFound, error
      when 512 # PBA account \w+ not found
        raise AccountNotFound, error
      when 513 # Invalid PBAAccountNumber/PBAConfirmationCode combination
        raise InvalidAccountAndConfirmation, error
      when 514 # Invalid AmountToPay
        raise InvalidAmount, error
      when 521 # PBAGlobalStatus is inactive
        raise GlobalStatusInactive, error
      when 522  # PBAJurisdictionStatus is inactive
        raise JurisdictionStatusInactive, error
      end
      super(message: error)
    end