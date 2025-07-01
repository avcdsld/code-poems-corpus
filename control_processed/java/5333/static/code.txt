@Override
	public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception {

		if (cause instanceof TransportException) {
			notifyAllChannelsOfErrorAndClose(cause);
		}
		else {
			final SocketAddress remoteAddr = ctx.channel().remoteAddress();

			final TransportException tex;

			// Improve on the connection reset by peer error message
			if (cause instanceof IOException
					&& cause.getMessage().equals("Connection reset by peer")) {

				tex = new RemoteTransportException(
						"Lost connection to task manager '" + remoteAddr + "'. This indicates "
								+ "that the remote task manager was lost.", remoteAddr, cause);
			}
			else {
				SocketAddress localAddr = ctx.channel().localAddress();
				tex = new LocalTransportException(
					String.format("%s (connection to '%s')", cause.getMessage(), remoteAddr),
					localAddr,
					cause);
			}

			notifyAllChannelsOfErrorAndClose(tex);
		}
	}