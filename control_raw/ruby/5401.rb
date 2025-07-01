def to_s
      pieces = []
      rd = recurrence_times_with_start_time - extimes
      pieces.concat rd.sort.map { |t| IceCube::I18n.l(t, format: IceCube.to_s_time_format) }
      pieces.concat rrules.map  { |t| t.to_s }
      pieces.concat exrules.map { |t| IceCube::I18n.t('ice_cube.not', target: t.to_s) }
      pieces.concat extimes.sort.map { |t|
        target = IceCube::I18n.l(t, format: IceCube.to_s_time_format)
        IceCube::I18n.t('ice_cube.not_on', target: target)
      }
      pieces.join(IceCube::I18n.t('ice_cube.pieces_connector'))
    end