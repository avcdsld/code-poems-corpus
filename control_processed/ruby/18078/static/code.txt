def mkdir(name)
      return self if name == '.'
      name = name[1..-1] if name[0] == '/'
      newdir, *remainder = name.split('/')
      subdir = get(newdir)
      unless subdir.dir?
        result = @od.request("#{api_path}/children",
          name: newdir,
          folder: {},
          '@microsoft.graph.conflictBehavior': 'rename'
        )
        subdir = OneDriveDir.new(@od, result)
      end
      remainder.any? ? subdir.mkdir(remainder.join('/')) : subdir
    end