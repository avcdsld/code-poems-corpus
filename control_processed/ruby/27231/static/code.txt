def bash(command = nil)
      Tempfile.open("tetra-history") do |history_file|
        Tempfile.open("tetra-bashrc") do |bashrc_file|
          kit = Tetra::Kit.new(@project)
          ant_path = kit.find_executable("ant")
          ant_in_kit = ant_path != nil
          ant_commandline = Tetra::Ant.commandline(@project.full_path, ant_path)

          mvn_path = kit.find_executable("mvn")
          mvn_in_kit = mvn_path != nil
          mvn_commandline = Tetra::Mvn.commandline(@project.full_path, mvn_path)

          bashrc_content = Bashrc.new(history_file.path, ant_in_kit, ant_commandline, mvn_in_kit, mvn_commandline).to_s
          log.debug "writing bashrc file: #{bashrc_file.path}"
          log.debug bashrc_content

          bashrc_file.write(bashrc_content)
          bashrc_file.flush

          if command
            run("bash --rcfile #{bashrc_file.path} -i -c '#{command}'")
            [command]
          else
            run_interactive("bash --rcfile #{bashrc_file.path} -i")
            history = File.read(history_file)
            log.debug "history contents:"
            log.debug history

            history.split("\n").map(&:strip)
          end
        end
      end
    end