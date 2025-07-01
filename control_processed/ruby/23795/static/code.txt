def submit_string(string, **kwargs)
      Tempfile.open('qsub.') do |f|
        f.write string.to_s
        f.close
        submit_script(f.path, **kwargs)
      end
    end