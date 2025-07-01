def merge(other)
      m1, t1 = resolved_modifier.downcase, resolved_type.downcase
      m2, t2 = other.resolved_modifier.downcase, other.resolved_type.downcase
      t1 = t2 if t1.empty?
      t2 = t1 if t2.empty?
      if (m1 == 'not') ^ (m2 == 'not')
        return if t1 == t2
        type = m1 == 'not' ? t2 : t1
        mod = m1 == 'not' ? m2 : m1
      elsif m1 == 'not' && m2 == 'not'
        # CSS has no way of representing "neither screen nor print"
        return unless t1 == t2
        type = t1
        mod = 'not'
      elsif t1 != t2
        return
      else # t1 == t2, neither m1 nor m2 are "not"
        type = t1
        mod = m1.empty? ? m2 : m1
      end
      Query.new([mod], [type], other.expressions + expressions)
    end