def unzip_to_tmp_dir_and_return_pathames_array(dir)
      zip_realpath = file.realpath
      Dir.chdir(dir) do
        if rar_archive?
          execute("unrar e -o+ #{zip_realpath}")
        else
          execute("unzip -o -j #{zip_realpath}")
        end
      end
      Pathname.new(dir).children
    end