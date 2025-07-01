def verify(otp, counter, retries: 0)
      counters = (counter..counter + retries).to_a
      counters.find do |c|
        super(otp, at(c))
      end
    end