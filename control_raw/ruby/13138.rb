def load_page
      @page ||= Language.current.pages.contentpages.find_by(
        urlname: params[:urlname],
        language_code: params[:locale] || Language.current.code
      )
    end