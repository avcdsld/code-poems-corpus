def add_to_zip(zip_stream)
      xml_string = write_xml
      return false if xml_string.empty?
      zip_stream.put_next_entry(RubyXL::from_root(self.xlsx_path))
      zip_stream.write(xml_string)
      true
    end