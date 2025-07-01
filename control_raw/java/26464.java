public void destorySession(Session session) {
        session.attributes().clear();
        sessionMap.remove(session.id());

        Event event = new Event();
        event.attribute("session", session);

        eventManager.fireEvent(EventType.SESSION_DESTROY, event);
    }