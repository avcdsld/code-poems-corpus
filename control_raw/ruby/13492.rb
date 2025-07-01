def key_by_file_and_line(review)
      warn_hash = {}
      review.warnings.each do |warning|
        filename = Pathname.new(warning.match[:filename]).cleanpath.to_s
        line_num = warning.match[:line].to_i
        warn_hash[filename] = {} unless warn_hash.key?(filename)
        unless warn_hash[filename].key?(line_num)
          warn_hash[filename][line_num] = Set.new
        end
        warn_hash[filename][line_num] << warning.rule
      end
      warn_hash
    end