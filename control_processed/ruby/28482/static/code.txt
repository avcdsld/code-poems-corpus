def seek_sky_conditions
      if observer.value == :auto # WMO 15.4
        if @chunks[0] == '///' or @chunks[0] == '//////'
          @chunks.shift # Simply dispose of it
          return
        end
      end

      loop do
        sky_condition = Metar::Data::SkyCondition.parse(@chunks[0])
        break if sky_condition.nil?
        @chunks.shift
        @sky_conditions << sky_condition
      end
    end