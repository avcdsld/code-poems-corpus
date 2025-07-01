def build_indicies
      specs = *map_gems_to_specs(gem_file_list)
      specs.select! { |s| s.class == ::Gem::Specification }
      ::Gem::Specification.dirs = []
      ::Gem::Specification.all = specs

      if ::Gem::VERSION >= '2.5.0'
        build_marshal_gemspecs specs
        build_modern_indices specs if @build_modern
        compress_indices
      else
        build_marshal_gemspecs
        build_modern_indicies if @build_modern
        compress_indicies
      end
    end