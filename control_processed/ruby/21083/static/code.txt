def build(build_name='default')
      description = Fudge::Parser.new.parse('Fudgefile')
      Fudge::Runner.new(description).run_build(build_name, options)
    end