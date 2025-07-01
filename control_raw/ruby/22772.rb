def create_empty_payment_profile(user)      
      options = {
        :customer_profile_id => user.authnet_customer_profile_id.to_i,      
        :payment_profile => {
          :bill_to => { :first_name => user.first_name, :last_name => user.last_name, :address => '', :city => '', :state => '', :zip => '', :phone_number => '', :email => user.email },        
          :payment => { :credit_card => Caboose::StdClass.new({ :number => '4111111111111111', :month => 1, :year => 2020, :first_name => user.first_name, :last_name => user.last_name }) }
        }
        #, :validation_mode => :live
      }    
      resp = self.gateway.create_customer_payment_profile(options)            
      if resp.success?        
        user.authnet_payment_profile_id = resp.params['customer_payment_profile_id']        
        user.save
      else
        puts "=================================================================="            
        puts resp.message
        puts ""
        puts resp.inspect
        puts "=================================================================="
      end
    end