@Override
    public void deliver(final OtpMsg msg) {
        final boolean delivered = self.deliver(msg);

        switch (msg.type()) {
        case OtpMsg.linkTag:
            if (delivered) {
                links.addLink(msg.getRecipientPid(), msg.getSenderPid());
            } else {
                try {
                    // no such pid - send exit to sender
                    super.sendExit(msg.getRecipientPid(), msg.getSenderPid(),
                            new OtpErlangAtom("noproc"));
                } catch (final IOException e) {
                }
            }
            break;

        case OtpMsg.unlinkTag:
        case OtpMsg.exitTag:
            links.removeLink(msg.getRecipientPid(), msg.getSenderPid());
            break;

        case OtpMsg.exit2Tag:
            break;
        }

        return;
    }