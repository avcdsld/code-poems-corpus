def to_xml
      xml = String.new('<cols>')

      @columns.each_with_index do |column, index|
        width_chars  = column[ :width_chars  ]
        width_pixels = column[ :width_pixels ]

        if width_chars.nil? && width_pixels.nil?
          xml << %Q{<col min="#{index + 1}" max="#{index + 1}"/>}
        else

          # https://msdn.microsoft.com/en-us/library/office/documentformat.openxml.spreadsheet.column.aspx
          #
          # Truncate(
          #   [{Number of Characters} * {Maximum Digit Width} + {5 pixel padding}]
          #   /{Maximum Digit Width}*256
          # )/256
          #
          # "Using the Calibri font as an example, the maximum digit width of
          #  11 point font size is 7 pixels (at 96 dpi)"
          #
          # By observation, though, I note that a different spreadsheet-wide
          # font size selected via the Workbook's ":font => { :size => ... }"
          # options Hash entry results in Excel, at least, scaling the given
          # widths in proportion with the requested font size change. We do
          # not, apparently, need to do that ourselves and run the calculation
          # based on the reference 11 point -> 7 pixel figure.
          #
          width_pixels ||= ((((width_chars * 7.0) + 5) / 7) * 256).truncate() / 256.0

          xml << %Q{<col min="#{index + 1}" max="#{index + 1}" width="#{width_pixels}" customWidth="1"/>}
        end
      end

      xml << '</cols>'
    end