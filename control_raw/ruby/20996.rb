def +(other)
      moment = @date_time.to_time.localtime(zone) + other.to_f.round(1)

      self.class.new(moment.strftime('%Y-%m-%dT%H:%M:%S.%N%:z'))
    end