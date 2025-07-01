def render_file(file, locs, opts, &block)
      _render_with_all_renderers(file[:relative_path].to_s, locs, self, opts, &block)
    end