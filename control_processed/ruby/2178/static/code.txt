def extract_script_nodes(list)
      list.select { |item| item.is_a?(::Sass::Script::Tree::Node) }
    end