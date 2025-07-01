def send_mail(klass, method, mail_params, send_params = nil)
      klass.new(send_params || params, self).dispatch_and_deliver(method, mail_params)
    end