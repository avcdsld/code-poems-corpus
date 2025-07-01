def compile_jst(paths)
      namespace   = Jammit.template_namespace
      paths       = paths.grep(Jammit.template_extension_matcher).sort
      base_path   = find_base_path(paths)
      compiled    = paths.map do |path|
        contents  = read_binary_file(path)
        contents  = contents.gsub(/\r?\n/, "\\n").gsub("'", '\\\\\'')
        name      = template_name(path, base_path)
        "#{namespace}['#{name}'] = #{Jammit.template_function}('#{contents}');"
      end
      compiler = Jammit.include_jst_script ? read_binary_file(DEFAULT_JST_SCRIPT) : '';
      setup_namespace = "#{namespace} = #{namespace} || {};"
      [JST_START, setup_namespace, compiler, compiled, JST_END].flatten.join("\n")
    end