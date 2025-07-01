def render(view)
      tags = []

      render_charset(tags)
      render_title(tags)
      render_icon(tags)
      render_with_normalization(tags, :description)
      render_with_normalization(tags, :keywords)
      render_refresh(tags)
      render_noindex(tags)
      render_alternate(tags)
      render_open_search(tags)
      render_links(tags)

      render_hashes(tags)
      render_custom(tags)

      tags.tap(&:compact!).map! { |tag| tag.render(view) }
      view.safe_join tags, MetaTags.config.minify_output ? "" : "\n"
    end