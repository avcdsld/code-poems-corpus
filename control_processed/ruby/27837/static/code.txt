def MUST!(m)
      RequirementLevel::High.new(m, false, subject, *challenges).result(true)
    end