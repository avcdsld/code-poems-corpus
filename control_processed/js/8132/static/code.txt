function releaseTriggeredEvent(oHandler) {
		if (!oHandler) {
			Log.error("Release trigger events must not be called without passing a valid handler!");
			return;
		}

		var mEventInfo = mTriggerEventInfo[oHandler.type];

		if (!mEventInfo) {
			return;
		} else if (!mEventInfo.domRefs[oHandler.id] || !mEventInfo.domRefs[oHandler.id].domRef) {
			Log.warning("Release trigger event for event type " + oHandler.type + "on Control " + oHandler.id + ": DomRef does not exists");
			return;
		}

		delete mEventInfo.domRefs[oHandler.id];
	}