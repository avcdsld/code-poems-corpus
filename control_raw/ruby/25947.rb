def to_html(template_filename)
      gameday_info = GamedayUtil.parse_gameday_id('gid_' + gid)
      template = ERB.new File.new(File.expand_path(File.dirname(__FILE__) + "/" + template_filename)).read, nil, "%"  
      return template.result(binding)
    end