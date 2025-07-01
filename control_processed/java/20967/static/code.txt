public void removeHttpSession(HttpSession session) {
		if (session == activeSession) {
			activeSession = null;
		}
		synchronized (this.sessions) {
			this.sessions.remove(session);
		}
		this.model.removeHttpSession(session);
		session.invalidate();
	}