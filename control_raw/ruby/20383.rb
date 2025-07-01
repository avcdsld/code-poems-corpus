def parse_markdown(markdown_string, renderer_options: {}, markdown_options: {}, image_options: {})
      markdown_string ||= ''
      markdown_opts = {
        no_intr_emphasis: true,
        tables: true,
        fenced_code_blocks: true,
        autolink: true,
        disable_indented_code_blocks: true,
        strikethrough: true,
        lax_spacing: true,
        space_after_headers: false,
        superscript: true,
        underline: true,
        highlight: true,
        footnotes: true
      }.merge(markdown_options)

      renderer_opts = {
        filter_html: false, # we want to allow HTML in the markdown blocks
        no_images: false,
        no_links: false,
        no_styles: false,
        escape_html: false,
        safe_links_only: false,
        with_toc_data: true,
        hard_wrap: true,
        xhtml: false,
        prettify: false,
        link_attributes: {},
        image_options: image_options
      }.merge(renderer_options)

      renderer = ContentfulRails::MarkdownRenderer.new(renderer_opts)
      markdown = Redcarpet::Markdown.new(renderer, markdown_opts)

      markdown.render(markdown_string).html_safe
    end