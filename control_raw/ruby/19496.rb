def convert_number(num)
    # Integer in the range 0..2**16-1
    if ((num =~ /^\d+$/) && (num.to_i <= 65535))
      return [@ptg['ptgInt'], num.to_i].pack("Cv")
    else  # A float
      num = [num.to_f].pack("d")
      num.reverse! if @byte_order
      return [@ptg['ptgNum']].pack("C") + num
    end
  end