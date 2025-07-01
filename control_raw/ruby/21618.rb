def trigger(m_wfid, m_error, m_action, msg, tracker)

      t_action = tracker['action']
      tracker_id = tracker['id']

      m = Ruote.fulldup(tracker['msg'])

      action = m.delete('action')

      m['wfid'] = m_wfid if m['wfid'] == 'replace'
      m['wfid'] ||= @context.wfidgen.generate

      m['workitem'] = msg['workitem'] if m['workitem'] == 'replace'

      if t_action == 'error_intercepted'
        m['workitem']['fields']['__error__'] = m_error
      elsif tracker_id == 'on_error' && m_action == 'error_intercepted'
        m['workitem']['fields']['__error__'] = m_error
      elsif tracker_id == 'on_terminate' && m_action == 'terminated'
        m['workitem']['fields']['__terminate__'] = { 'wfid' => m_wfid }
      end

      if m['variables'] == 'compile'
        fexp = Ruote::Exp::FlowExpression.fetch(@context, msg['fei'])
        m['variables'] = fexp ? fexp.compile_variables : {}
      end

      @context.storage.put_msg(action, m)
    end