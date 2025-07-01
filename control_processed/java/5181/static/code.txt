@Nullable
	MultiTaskSlot getUnresolvedRootSlot(AbstractID groupId) {
		for (MultiTaskSlot multiTaskSlot : unresolvedRootSlots.values()) {
			if (!multiTaskSlot.contains(groupId)) {
				return multiTaskSlot;
			}
		}

		return null;
	}