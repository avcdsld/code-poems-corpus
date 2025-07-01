def url
      @url ||= begin
        base = if @collection.nil?
                 cleaned_relative_path
               else
                 Jekyll::URL.new(
                   :template     => @collection.url_template,
                   :placeholders => placeholders
                 )
               end.to_s.chomp("/")
        base << extname
      end
    end