def set
      unless stack = Codex.in(shift_argument)
        error("Usage: heroku stack:set STACK.\nMust specify target stack.")
      end

      api.put_stack(app, stack)
      display "Stack set. Next release on #{app} will use #{Codex.out(stack)}."
      display "Run `git push heroku master` to create a new release on #{Codex.out(stack)}."
    end