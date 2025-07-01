def calculated_sign
      params = SIGN_PARAMS.each_with_object({}) do |p, h|
        h[p] = send(p).tap { |v| v ? v.to_s : nil }
      end
      Signature.new(params, @secret).sign.upcase
    end