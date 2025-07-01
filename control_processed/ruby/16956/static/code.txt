def sections_are_all_valid
      sections.each do |section|
        unless section.valid?
          errors.add :base, section.errors.messages[:base]
        end
      end
    end