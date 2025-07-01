def build(file)
      manifest = YAML.load_file file
      raise CFManifests::InvalidManifest.new(file) unless manifest

      Array(manifest["inherit"]).each do |path|
        manifest = merge_parent(path, manifest)
      end

      manifest.delete("inherit")

      manifest
    end