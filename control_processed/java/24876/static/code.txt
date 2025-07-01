public void write_port(final String node, final int id, final int creation) {
	write1(OtpExternal.portTag);
	write_atom(node);
	write4BE(id & 0xfffffff); // 28 bits
	write1(creation & 0x3); // 2 bits
    }