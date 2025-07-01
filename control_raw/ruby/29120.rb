def config_server
      file = File.open("#{@project_name}/server.rb", "r+")
      file.each do |line|	   
        while line == "  def response(env)\n" do
          pos = file.pos
          rest = file.read
          file.seek pos
          file.write("\t::") 
          file.write(@module_name)
          file.write("::Base.call(env)\n")
          file.write(rest)
          $stdout.puts "\e[1;35m \tconfig\e[0m\tserver.rb"
          return
        end
      end
    end