def write(tag, protocol, lock=false)
      tmp = lock ? 1 : 0
	  Klass.write(@handle, tag,  Phidgets::FFI::RFIDTagProtocol[protocol], tmp)
	  true
	end