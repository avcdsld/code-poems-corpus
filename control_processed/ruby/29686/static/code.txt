def run_all
      Compat::UI.info 'Guard::Less: compiling all files'
      files = Dir.glob('**/*.*')
      paths = Compat.matching_files(self, files).uniq
      run(paths)
    end