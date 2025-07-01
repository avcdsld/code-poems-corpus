def activated_by?(string_to_page, inspect_mode=false)
      inspect_mode ? (String.size(string_to_page) > @height * @width) : (string_to_page.count("\n") > @height)
    end