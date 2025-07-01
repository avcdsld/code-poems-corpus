def to_hash
      hash = {
        :slug         => slug, 
        :permalink    => permalink, 
        :name         => name, 
        :children     => children,
        :siblings     => siblings,
        :parent       => parent, 
        :ancestors    => ancestors,
        :navigation   => Bonsai::Navigation.tree,
        :updated_at   => mtime,
        :created_at   => ctime
      }.merge(formatted_content).merge(disk_assets).merge(Bonsai.site)
      
      hash.stringify_keys
    end