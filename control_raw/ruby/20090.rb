def write_sheet_pr # :nodoc:

      attributes = []

      attributes << ['filterMode', 1] if ptrue?(@filter_on)

      if ptrue?(@fit_page) || ptrue?(@tab_color)
        @writer.tag_elements('sheetPr', attributes) do
          write_tab_color
          write_page_set_up_pr
        end
      else
        @writer.empty_tag('sheetPr', attributes)
      end
    end