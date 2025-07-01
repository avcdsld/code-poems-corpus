def handle_sections(str)
         sectionSplit = str.split(" ")
         if sectionSplit.size == 4
            section = Sections.new
            section.address = sectionSplit[0]
            section.size = sectionSplit[1]
            section.segment = sectionSplit[2]
            section.section = sectionSplit[3]
            l_sections << section
         end
      end