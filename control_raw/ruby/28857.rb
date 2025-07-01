def banner(msg, size = :normal, colour = :black)
      return unless msg
      banners = {
        :huge => Rudy::Utils.without_indent(%Q(
        =======================================================
        =======================================================
        !!!!!!!!!   %s   !!!!!!!!!
        =======================================================
        =======================================================)),
        :normal => %Q(============  %s  ============)
      }
      size = :normal unless banners.has_key?(size)
      #colour = :black unless Drydock::Console.valid_colour?(colour)
      size, colour = size.to_sym, colour.to_sym
      sprintf(banners[size], msg).bright.att(:reverse)
    end