def fast_access_funding(options)
      transaction = FastAccessFunding.new
      transaction.reportGroup = get_report_group(options)
      transaction.transactionId = options['id']
      transaction.customerId = options['customerId']

      transaction.fundingSubmerchantId    = options['fundingSubmerchantId']
      transaction.submerchantName         = options['submerchantName']
      transaction.fundsTransferId         = options['fundsTransferId']
      transaction.amount                  = options['amount']

      transaction.card                    = Card.from_hash(options)
      transaction.token                   = CardToken.from_hash(options,'token')
      transaction.paypage                 = CardPaypage.from_hash(options,'paypage')

      return transaction
    end