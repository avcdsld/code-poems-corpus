def cancel_process(msg)

      root = @storage.find_root_expression(msg['wfid'])

      return unless root

      @storage.put_msg(
        'cancel',
        'fei' => root['fei'],
        'wfid' => msg['wfid'], # indicates this was triggered by cancel_process
        'flavour' => msg['flavour'])
    end