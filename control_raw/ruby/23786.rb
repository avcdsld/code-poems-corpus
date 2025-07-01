def connect(&block)
      Torque.lib = lib.join('libtorque.so')
      cid = Torque.pbs_connect(host)
      Torque.raise_error(cid.abs) if cid < 0  # raise error if negative connection id
      begin
        value = yield cid
      ensure
        Torque.pbs_disconnect(cid)            # always close connection
      end
      Torque.check_for_error                  # check for errors at end
      value
    end