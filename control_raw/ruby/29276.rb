def judge(text)
      Song.new(parser.parse(text), exactly: true, rule: @rule).valid?
    end