def jasmine_js_files
      files = Jasmine::Core.js_files
      files << jasmine_boot_file
      files += JasmineRails.reporter_files params[:reporters]
      files << 'jasmine-specs.js'
      files
    end