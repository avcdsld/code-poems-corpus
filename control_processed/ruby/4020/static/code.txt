def mytoc
      @title = CGI.escapeHTML(@producer.res.v('toctitle'))

      @body = %Q(  <h1 class="toc-title">#{CGI.escapeHTML(@producer.res.v('toctitle'))}</h1>\n)
      if @producer.config['epubmaker']['flattoc'].nil?
        @body << hierarchy_ncx('ul')
      else
        @body << flat_ncx('ul', @producer.config['epubmaker']['flattocindent'])
      end

      @language = @producer.config['language']
      @stylesheets = @producer.config['stylesheet']
      tmplfile = if @producer.config['htmlversion'].to_i == 5
                   File.expand_path('./html/layout-html5.html.erb', ReVIEW::Template::TEMPLATE_DIR)
                 else
                   File.expand_path('./html/layout-xhtml1.html.erb', ReVIEW::Template::TEMPLATE_DIR)
                 end
      tmpl = ReVIEW::Template.load(tmplfile)
      tmpl.result(binding)
    end