def schedule_retries(handler, err)

      retries = handler.split(/\s*,\s*/)

      after, action = retries.shift.split(/:/)
      (after, action = '0', after) if action.nil?

      # deal with "* 3"

      if m = action.match(/^ *([^ ]+) *\* *(\d+)$/)

        count = m[2].to_i - 1

        if count == 1
          retries.unshift("#{after}: #{m[1]}")
        elsif count > 1
          retries.unshift("#{after}: #{m[1]} * #{count}")
        end
      end

      # rewrite tree to remove current retry

      t = Ruote.fulldup(tree)

      if h.on_error.is_a?(Array)
        handler.update_tree(t, retries)
      else
        if retries.empty?
          t[1].delete('on_error')
        else
          t[1]['on_error'] = retries.join(', ')
        end
      end

      update_tree(t)

      # schedule current retry

      after = after.strip
      action = action.strip

      msg = {
        'action' => 'cancel',
        'fei' => h.fei,
        'flavour' => 'retry',
        're_apply' => true }

      (h.timers ||= []) <<
        [ @context.storage.put_schedule('at', h.fei, after, msg), 'retry' ]

      # over

      persist_or_raise

    rescue => e

      raise Ruote::MetaError.new(__method__.to_s, e)
    end