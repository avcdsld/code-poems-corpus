def strand( len=8, safe=true )
       chars = ("a".."z").to_a + ("0".."9").to_a
       chars.delete_if { |v| %w(i l o 1 0).member?(v) } if safe
       str = ""
       1.upto(len) { |i| str << chars[rand(chars.size-1)] }
       str
    end