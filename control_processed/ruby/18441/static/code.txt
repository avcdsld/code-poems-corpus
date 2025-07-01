def to_s
      ret = Helper.color(format("#<%s:%#x>\n", self.class.to_s, @base), sev: :klass)
      ret += "flags = [#{flags.map { |f| Helper.color(":#{f}", sev: :sym) }.join(',')}]\n"
      ret += "size = #{Helper.color(format('%#x', size))} (#{bintype})\n"
      ret += "prev_size = #{Helper.color(format('%#x', @prev_size))}\n" unless flags.include? :prev_inuse
      ret += "data = #{Helper.color(@data.inspect)}#{'...' if @data.length < size - size_t * 2}\n"
      ret
    end