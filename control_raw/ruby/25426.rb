def write_data_elements(elements)
      elements.each do |element|
        # If this particular element has children, write these (recursively) before proceeding with elements at the current level:
        if element.is_parent?
          if element.children?
            # Sequence/Item with child elements:
            element.reset_length unless @enc_image
            write_data_element(element)
            write_data_elements(element.children)
            if @enc_image
              # Write a delimiter for the pixel tag, but not for its items:
              write_delimiter(element) if element.tag == PIXEL_TAG
            else
              write_delimiter(element)
            end
          else
            # Parent is childless:
            if element.bin
              write_data_element(element) if element.bin.length > 0
            elsif @include_empty_parents
              # Only write empty/childless parents if specifically indicated:
              write_data_element(element)
              write_delimiter(element)
            end
          end
        else
          # Ordinary Data Element:
          if element.tag.group_length?
            # Among group length elements, only write the meta group element (the others have been retired in the DICOM standard):
            write_data_element(element) if element.tag == "0002,0000"
          else
            write_data_element(element)
          end
        end
      end
    end