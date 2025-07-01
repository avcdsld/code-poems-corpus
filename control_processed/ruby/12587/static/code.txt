def _dependencies(seen, engines)
      key = [@options[:filename], @options[:importer]]
      return if seen.include?(key)
      seen << key
      engines << self
      to_tree.grep(Tree::ImportNode) do |n|
        next if n.css_import?
        n.imported_file._dependencies(seen, engines)
      end
    end