def select_styles(*styles)
      styles.tap(&:compact).flatten!
      if styles.empty? or styles.length == 1 && /\Anone\z/io.match(styles[0])
        return :NONE
      end
      styles.select { |s| FONT_STYLE.match(s) }
    end