def layout_for(document)
      if index?(document) && layout_exists?("home")
        "home"
      elsif page?(document) && layout_exists?("page")
        "page"
      elsif post?(document) && layout_exists?("post")
        "post"
      elsif layout_exists?("default")
        "default"
      end
    end