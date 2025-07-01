def gen_class_index
      gen_an_index(@classes, 'All Classes', RDoc::Page::CLASS_INDEX, "fr_class_index.html")
      @allfiles.each do |file|
        unless file['file'].context.file_relative_name =~ /\.rb$/

          gen_composite_index(
            file,
              RDoc::Page::COMBO_INDEX,

              "#{MODULE_DIR}/fr_#{file["file"].context.module_name}.html")
        end
      end
    end