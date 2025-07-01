def write_delimiter(element)
      delimiter_tag = (element.tag == ITEM_TAG ? ITEM_DELIMITER : SEQUENCE_DELIMITER)
      write_tag(delimiter_tag)
      write_vr_length(delimiter_tag, ITEM_VR, 0)
    end