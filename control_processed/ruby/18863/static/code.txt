def import(cert, password)
      cmd = Xcode::Shell::Command.new "security"
      cmd << "import '#{cert}'"
      cmd << "-k \"#{@path}\""
      cmd << "-P #{password}"
      cmd << "-T /usr/bin/codesign"
      cmd.execute
    end