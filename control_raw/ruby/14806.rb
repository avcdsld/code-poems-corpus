def local_time(year, month = 1, day = 1, hour = 0, minute = 0, second = 0, sub_second = 0, dst = Timezone.default_dst, &block)
      local_timestamp(year, month, day, hour, minute, second, sub_second, dst, &block).to_time
    end