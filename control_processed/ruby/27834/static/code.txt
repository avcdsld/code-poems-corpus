def note_tag(file)
      digest = Digest::SHA1.new
      File.open(file) {|f| digest << f.read(4096) }
      repo = @repository.clone
      repo.tag = digest.hexdigest
      @repository = repo
    end