def language_links(options = {})
      options = {
        linkname: 'name',
        show_title: true,
        spacer: '',
        reverse: false
      }.merge(options)
      languages = Language.on_current_site.published.with_root_page.order("name #{options[:reverse] ? 'DESC' : 'ASC'}")
      return nil if languages.count < 2
      render(
        partial: "alchemy/language_links/language",
        collection: languages,
        spacer_template: "alchemy/language_links/spacer",
        locals: {languages: languages, options: options}
      )
    end