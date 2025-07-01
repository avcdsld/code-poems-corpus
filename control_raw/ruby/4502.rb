def curp
      all_letters = CONSONANTS + VOWELS
      hm = %w[H M]
      date = ::Time.at(rand * ::Time.now.to_f).strftime('%y%m%d')
      [
        fetch_sample(CONSONANTS),
        fetch_sample(VOWELS),
        fetch_sample(all_letters, count: 2).join,
        date,
        fetch_sample(hm),
        fetch_sample(ESTADOS_CURP),
        fetch_sample(CONSONANTS, count: 3).join,
        fetch_sample(HOMOCLAVE),
        rand(0..9)
      ].join
    end