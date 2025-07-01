def seconds_until_epoch(epoch)
        sec = (epoch - Time.now.to_f).ceil
        sec = 0 if sec < 0
        sec
      end