def authorize_and_capture
      
      resp = StdClass.new                        
      if self.financial_status == Invoice::FINANCIAL_STATUS_CAPTURED
        resp.error = "Funds for this invoice have already been captured."
      else
                        
        sc = self.site.store_config                
        case sc.pp_name                                    
          when StoreConfig::PAYMENT_PROCESSOR_STRIPE
                                                                              
            Stripe.api_key = sc.stripe_secret_key.strip
            bt = nil
            begin
              c = Stripe::Charge.create(
                :amount => (self.total * 100).to_i,
                :currency => 'usd',
                :customer => self.customer.stripe_customer_id,
                :capture => true,
                :metadata => { :invoice_id => self.id },
                :statement_descriptor => "#{self.site.description.truncate(22)}"
              )                        
            rescue Exception => ex
              resp.error = "Error during capture process\n#{ex.message}"                
            end            
            if resp.error.nil?
              InvoiceTransaction.create(
                :invoice_id => self.id,
                :transaction_id => c.id,
                :transaction_type => InvoiceTransaction::TYPE_AUTHCAP,
                :payment_processor => sc.pp_name,
                :amount => c.amount / 100.0,
                :captured => true,
                :date_processed => DateTime.now.utc,
                :success => c.status == 'succeeded'
              )
              if c.status == 'succeeded'
                self.financial_status = Invoice::FINANCIAL_STATUS_CAPTURED
                self.save
                resp.success = true
              else
                resp.error = "Error capturing funds."
              end
            end
                      
        end        
      end      
      return resp
    end