def handle_map
         handle_method_name = ""
         File.read(@l_name).each_line do |line|
            if line[0] == "#"
               if line.include?("Path:")
                  handle_method_name =  "get_path"
                  puts "处理path..."
               elsif line.include?("Arch:")
                  handle_method_name = "get_arch"
                  puts "处理Arch..."
               elsif line.include?("Object files")
                  handle_method_name = "handle_ojbect_files"
                  puts "处理Object files..."
               elsif line.include?("Sections")
                  handle_method_name = "handle_sections"
                  puts "处理Sections..."
               elsif line.include?("Symbols:")   #symbols:和Dead Stripped Symbols处理一样
               #   这里不处理Dead Stripped Symbols
                  if line.delete('#').strip.include?("Dead Stripped Symbols")
                     puts "不处理处理#{line.delete('#').strip}..."
                     break
                  end
                  puts "处理#{line.delete('#').strip}..."
                  handle_method_name = "handle_symbols"
               end
            end
            self.send(handle_method_name, line)

         end
      end