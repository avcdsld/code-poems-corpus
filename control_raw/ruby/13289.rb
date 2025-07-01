def write(dir)
      FileUtils.mkdir(dir) unless File.exists?(dir)
      each_item {|guide| write_guide(guide, dir) }
    end