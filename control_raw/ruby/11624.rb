def to_html(options = :DEFAULT, extensions = [])
      opts = Config.process_options(options, :render)
      _render_html(opts, extensions).force_encoding('utf-8')
    end