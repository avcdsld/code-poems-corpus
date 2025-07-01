def capture(amount = nil)
      
      return { :error => "This invoice doesn't seem to be authorized." } if !self.success
      
      ct = InvoiceTransaction.where(:parent_id => self.id, :transaction_type => InvoiceTransaction::TYPE_CAPTURE, :success => true).first      
      return { :error => "Funds for this invoice have already been captured." } if ct
      
      # Make sure the amount given isn't greater than the invoice total      
      return { :error => "Amount given to capture is greater than the current invoice total." } if amount && amount.to_f > self.invoice.total.to_f        
      amount = self.invoice.total if amount.nil?      
            
      resp = Caboose::StdClass.new
      sc = self.invoice.site.store_config                
      case sc.pp_name
                                  
        when StoreConfig::PAYMENT_PROCESSOR_STRIPE
                                                                                    
          Stripe.api_key = sc.stripe_secret_key.strip
          bt = nil
          begin            
            c = Stripe::Charge.retrieve(self.transaction_id)            
            return { :error => "Amount given to capture is greater than the amount authorized. amount = #{amount}, c.amount = #{c.amount}" } if (amount*100).to_i > c.amount            
            amount = (amount.to_f * 100.0).to_i
            if amount == c.amount              
              c = c.capture
            else
              c = c.capture({ :amount => amount })
            end
            bt = Stripe::BalanceTransaction.retrieve(c.balance_transaction)
          rescue Exception => ex
            resp.error = "Error during capture process\n#{ex.message}"                
          end
          
          if resp.error.nil?
            InvoiceTransaction.create(
              :invoice_id => self.invoice_id,
              :parent_id => self.id,
              :transaction_id => bt.id,
              :transaction_type => InvoiceTransaction::TYPE_CAPTURE,
              :payment_processor => sc.pp_name,
              :amount => bt.amount / 100.0,                
              :date_processed => DateTime.strptime(bt.created.to_s, '%s'),
              :success => bt.status == 'succeeded' || bt.status == 'pending'
            )
            if bt.status == 'succeeded' || bt.status == 'pending'
              self.captured = true
              self.save              
              self.invoice.financial_status = Invoice::FINANCIAL_STATUS_CAPTURED
              self.invoice.save
              resp.success = true
            else
              resp.error = "Error capturing funds."
            end
          end
          
      end
      return resp
      
    end