def number_pages(options = {})
      opt = {
        number_format: ' - %s - ',
        start_at: 1,
        font: :Helvetica,
        margin_from_height: 45,
        margin_from_side: 15
      }
      opt.update options
      opt[:location] ||= opt[:number_location] ||= opt[:stamp_location] ||= [:top, :bottom]
      opt[:location] = [opt[:location]] unless opt[:location].is_a? Array

      page_number = opt[:start_at]
      format_repeater = opt[:number_format].count('%')
      just_center = [:center]
      small_font_size = opt[:font_size] || 12

      # some common computations can be done only once.
      from_height = opt[:margin_from_height]
      from_side = opt[:margin_from_side]
      left_position = from_side

      (opt[:page_range] ? pages[opt[:page_range]] : pages).each do |page|
        # Get page dimensions
        mediabox = page[:CropBox] || page[:MediaBox] || [0, 0, 595.3, 841.9]
        # set stamp text
        text = opt[:number_format] % (Array.new(format_repeater) { page_number })
        if opt[:location].include? :center
          add_opt = {}
          if opt[:margin_from_height] && !opt[:height] && !opt[:y]
            add_opt[:height] = mediabox[3] - mediabox[1] - (2 * opt[:margin_from_height].to_f)
            add_opt[:y] = opt[:margin_from_height]
          end
          if opt[:margin_from_side] && !opt[:width] && !opt[:x]
            add_opt[:width] = mediabox[2] - mediabox[0] - (2 * opt[:margin_from_side].to_f)
            add_opt[:x] = opt[:margin_from_side]
          end
          page.textbox text, opt.merge(add_opt)
        end
        unless opt[:location] == just_center
          add_opt = { font_size: small_font_size }.merge(opt)
          # text = opt[:number_format] % page_number
          # compute locations for text boxes
          text_dimantions = Fonts.dimensions_of(text, opt[:font], small_font_size)
          box_width = text_dimantions[0] * 1.2
          box_height = text_dimantions[1] * 2
          page_width = mediabox[2]
          page_height = mediabox[3]

          add_opt[:width] ||= box_width
          add_opt[:height] ||= box_height

          center_position = (page_width - box_width) / 2
          right_position = page_width - from_side - box_width
          top_position = page_height - from_height
          bottom_position = from_height + box_height

          if opt[:location].include? :top
            page.textbox text, { x: center_position, y: top_position }.merge(add_opt)
          end
          if opt[:location].include? :bottom
            page.textbox text, { x: center_position, y: bottom_position }.merge(add_opt)
          end
          if opt[:location].include? :top_left
            page.textbox text, { x: left_position, y: top_position, font_size: small_font_size }.merge(add_opt)
          end
          if opt[:location].include? :bottom_left
            page.textbox text, { x: left_position, y: bottom_position, font_size: small_font_size }.merge(add_opt)
          end
          if opt[:location].include? :top_right
            page.textbox text, { x: right_position, y: top_position, font_size: small_font_size }.merge(add_opt)
          end
          if opt[:location].include? :bottom_right
            page.textbox text, { x: right_position, y: bottom_position, font_size: small_font_size }.merge(add_opt)
          end
        end
        page_number = page_number.succ
      end
    end