def render(document)
      renderer = find_renderer(document)
      renderer.render(document) unless renderer.nil?
    end