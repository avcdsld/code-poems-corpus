def request_params
      case account_type
      when AccountType::MANAGED
        managed_request_params
      when AccountType::FEDERATED
        federated_request_params
      else
        fail UnsupportedAccountTypeError, account_type
      end
    end