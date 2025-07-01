def make_sseq(subject, *sseqs)
      make_seq(Sass::Selector::SimpleSequence.new(sseqs, subject))
    end