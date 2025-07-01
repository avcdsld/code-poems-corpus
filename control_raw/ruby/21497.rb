def do_cancel(msg)

      flavour = msg['flavour']

      return if h.state == 'cancelling' && flavour != 'kill'
        # cancel on cancel gets discarded

      return if h.state == 'failed' && flavour == 'timeout'
        # do not timeout expressions that are "in error" (failed)

      h.state = case flavour
        when 'kill' then 'dying'
        when 'timeout' then 'timing_out'
        else 'cancelling'
      end

      if h.state == 'timing_out'

        h.applied_workitem['fields']['__timed_out__'] = [
          h.fei, Ruote.now_to_utc_s, tree.first, compile_atts
        ]

      elsif h.state == 'cancelling'

        if t = msg['on_cancel']

          h.on_cancel = t

        elsif ra_opts = msg['re_apply']

          ra_opts = {} if ra_opts == true
          ra_opts['tree'] ||= tree

          h.on_re_apply = ra_opts
        end
      end

      cancel(flavour)
    end