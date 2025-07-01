def mkcomments(commentfile)
      unless commentfile.nil?
        comms = Comments.new()
        File.open(@destination + '/xl/'+commentfile.gsub('../', ''), 'r') do |f|
          Ox.sax_parse(comms, f)
        end
        return comms.commarray
      end
    end