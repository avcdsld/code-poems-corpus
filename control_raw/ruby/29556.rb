def ask_stage
      question = I18n.t :ask_stage_name, scope: :negroku
      stage_name = Ask.input question
      raise "Stage name required" if stage_name.empty?
      stage_name
    end