def generate_initialization_vector(words)
    srand(Time.now.to_i)
    vector = ""
    words.times {
      vector << [rand(ULONG)].pack('N')
    }
    return(vector)
  end