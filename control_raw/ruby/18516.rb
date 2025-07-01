def timeline_min
      @js = ""
      @css = Kompress::CSS.new(File.open("#{TimelineSetter::ROOT}/public/stylesheets/timeline-setter.css").read).css
      libs = Dir.glob("#{TimelineSetter::ROOT}/public/javascripts/vendor/**").select {|q| q =~ /min/ }
      libs.each { |lib| @js << File.open(lib,'r').read }
      @min_html = Kompress::HTML.new(timeline_markup).html
      @js << File.open("#{TimelineSetter::ROOT}/public/javascripts/timeline-setter.min.js", 'r').read
      @timeline = tmpl("timeline-min.erb")
    end