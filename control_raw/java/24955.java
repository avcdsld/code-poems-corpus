public OtpErlangRef read_ref() throws OtpErlangDecodeException {
        String node;
        int id;
        int creation;
        int tag;

        tag = read1skip_version();

        switch (tag) {
        case OtpExternal.refTag:
            node = read_atom();
            id = read4BE() & 0x3ffff; // 18 bits
            creation = read1() & 0x03; // 2 bits
            return new OtpErlangRef(node, id, creation);

        case OtpExternal.newRefTag:
        case OtpExternal.newerRefTag:
            final int arity = read2BE();
            if (arity > 3) {
		throw new OtpErlangDecodeException(
		    "Ref arity " + arity + " too large ");
	    }
            node = read_atom();
	    if (tag == OtpExternal.newRefTag)
		creation = read1();
	    else
		creation = read4BE();

            final int[] ids = new int[arity];
            for (int i = 0; i < arity; i++) {
                ids[i] = read4BE();
            }
            return new OtpErlangRef(tag, node, ids, creation);

        default:
            throw new OtpErlangDecodeException(
                    "Wrong tag encountered, expected ref, got " + tag);
        }
    }