public boolean ping(final String anode, final long timeout) {
        if (anode.equals(node)) {
            return true;
        } else if (anode.indexOf('@', 0) < 0
                && anode.equals(node.substring(0, node.indexOf('@', 0)))) {
            return true;
        }

        // other node
        OtpMbox mbox = null;
        try {
            mbox = createMbox();
            mbox.send("net_kernel", anode, getPingTuple(mbox));
            final OtpErlangObject reply = mbox.receive(timeout);

            final OtpErlangTuple t = (OtpErlangTuple) reply;
            final OtpErlangAtom a = (OtpErlangAtom) t.elementAt(1);
            return "yes".equals(a.atomValue());
        } catch (final Exception e) {
        } finally {
            closeMbox(mbox);
        }
        return false;
    }