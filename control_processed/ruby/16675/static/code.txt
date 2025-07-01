def post(path, data, initheader = nil, dest = nil, &block) # :yield: +body_segment+
      res = nil
      request(Post.new(path, initheader), data) {|r|
        r.read_body dest, &block
        res = r
      }
      unless @newimpl
        res.value
        return res, res.body
      end
      res
    end