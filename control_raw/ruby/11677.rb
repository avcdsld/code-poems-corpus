def eat_phrase
    phrase = [:or, eat_subphrase]
    while eat_word("or"); phrase << eat_subphrase end
    phrase.length == 2 ? phrase[1] : phrase
  end