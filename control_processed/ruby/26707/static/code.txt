def show
      @script_authors = Script::Author.friendly.find(params[:id])
      @versions = Phcscriptcdn::AuthorVersions.where(item_id: params[:id], item_type: 'Phcscriptcdn::Script::Author')
    end