def swift_national_id
      return if swift_bank_code.nil? && swift_branch_code.nil?

      national_id = swift_bank_code.to_s
      national_id += swift_branch_code.to_s
      national_id.slice(0, structure[:national_id_length])
    end