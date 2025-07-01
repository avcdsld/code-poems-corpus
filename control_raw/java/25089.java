@Override public TimelineV3 fillFromImpl(Timeline timeline) {
    ArrayList<EventV3> outputEvents = new ArrayList<>();
    ArrayList<TimelineSnapshot.Event> heartbeats = new ArrayList();
    H2O cloud = TimeLine.getCLOUD();

    if (null != timeline.snapshot) {
      for (TimelineSnapshot.Event event : timeline.snapshot) {
        H2ONode h2o = cloud.members()[event._nodeId];
        // The event type.  First get payload.
        UDP.udp msgType = event.udpType();
        // Accumulate repeated heartbeats
        if (msgType == UDP.udp.heartbeat) {
          heartbeats.add(event);
          continue;
        }
        // Now dump out accumulated heartbeats
        if (!heartbeats.isEmpty()) {
          long firstMs = heartbeats.get(0).ms();
          long lastMs = heartbeats.get(heartbeats.size() - 1).ms();
          int totalSends = 0;
          int totalRecvs = 0;
          int totalDrops = 0;
          int[] sends = new int[cloud.size()];
          int[] recvs = new int[cloud.size()];
          for (TimelineSnapshot.Event h : heartbeats) {
            if (h.isSend()) {
              ++totalSends;
              ++sends[h._nodeId];
            } else if (h.isDropped()) {
              ++totalDrops;
            } else {
              ++totalRecvs;
              ++recvs[h._nodeId];
            }
          }
          heartbeats.clear();
          outputEvents.add(new HeartBeatEvent(totalSends, totalRecvs, firstMs, lastMs));
        }
        long ms = event.ms();
        long ns = event.ns();
        if (msgType == UDP.udp.i_o) { // handle io event
          outputEvents.add(new IOEvent(ms, ns, event.recoH2O().toString(), event.ioflavor(), UDP.printx16(event.dataLo(), event.dataHi())));
        } else { // network msg
          String from, to;
          if (event.isSend()) {
            from = h2o.toString();
            to = event.packH2O() == null ? "multicast" : event.packH2O().toString();
          } else {
            from = event.packH2O().toString();
            to = h2o.toString();
          }
          outputEvents.add(new NetworkEvent(ms, ns, event.isSend(), event.isTCP() ? "TCP" : "UDP", msgType.toString(), from, to, UDP.printx16(event.dataLo(), event.dataHi())));
        }
      }
    } // if timeline.snapshot
    events = outputEvents.toArray(new EventV3[null == outputEvents ? 0 : outputEvents.size()]);
    return this;
  }