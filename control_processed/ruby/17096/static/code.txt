def imode_browser_version
      case @request.env['HTTP_USER_AGENT']
      when %r{^DoCoMo/1.0/}
        ver = '1.0'
      when %r{^DoCoMo/2.0 }
        @request.env['HTTP_USER_AGENT'] =~ / (\w+)\(c(\d+);/
        model = Regexp.last_match(1)
        cache_size = Regexp.last_match(2).to_i

        ver = if cache_size >= 500
                (%w[P03B P05B L01B].member?(model) ? '2.0LE' : '2.0')
              else
                '1.0'
              end
      else
        # DoCoMo/3.0以降等は、とりあえず非v1.0扱い
        ver = '2.0'
      end

      ver
    end