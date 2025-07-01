def prepare_vml_objects  #:nodoc:
      comment_id     = 0
      vml_drawing_id = 0
      vml_data_id    = 1
      vml_header_id  = 0
      vml_shape_id   = 1024
      comment_files  = 0
      has_button     = false

      @worksheets.each do |sheet|
        next if !sheet.has_vml? && !sheet.has_header_vml?
        if sheet.has_vml?
          if sheet.has_comments?
            comment_files += 1
            comment_id    += 1
          end
          vml_drawing_id += 1

          sheet.prepare_vml_objects(vml_data_id, vml_shape_id,
                                    vml_drawing_id, comment_id)

          # Each VML file should start with a shape id incremented by 1024.
          vml_data_id  +=    1 * ( 1 + sheet.num_comments_block )
          vml_shape_id += 1024 * ( 1 + sheet.num_comments_block )
        end

        if sheet.has_header_vml?
          vml_header_id  += 1
          vml_drawing_id += 1
          sheet.prepare_header_vml_objects(vml_header_id, vml_drawing_id)
        end

        # Set the sheet vba_codename if it has a button and the workbook
        # has a vbaProject binary.
        unless sheet.buttons_data.empty?
          has_button = true
          if @vba_project && !sheet.vba_codename
            sheet.set_vba_name
          end
        end
      end

      add_font_format_for_cell_comments if num_comment_files > 0

      # Set the workbook vba_codename if one of the sheets has a button and
      # the workbook has a vbaProject binary.
      if has_button && @vba_project && !@vba_codename
        set_vba_name
      end
    end