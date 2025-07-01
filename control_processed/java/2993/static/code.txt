protected SimpleSlot getNewSlotForSharingGroup(ExecutionVertex vertex,
													Iterable<TaskManagerLocation> requestedLocations,
													SlotSharingGroupAssignment groupAssignment,
													CoLocationConstraint constraint,
													boolean localOnly)
	{
		// we need potentially to loop multiple times, because there may be false positives
		// in the set-with-available-instances
		while (true) {
			Pair<Instance, Locality> instanceLocalityPair = findInstance(requestedLocations, localOnly);
			
			if (instanceLocalityPair == null) {
				// nothing is available
				return null;
			}

			final Instance instanceToUse = instanceLocalityPair.getLeft();
			final Locality locality = instanceLocalityPair.getRight();

			try {
				JobVertexID groupID = vertex.getJobvertexId();
				
				// allocate a shared slot from the instance
				SharedSlot sharedSlot = instanceToUse.allocateSharedSlot(groupAssignment);

				// if the instance has further available slots, re-add it to the set of available resources.
				if (instanceToUse.hasResourcesAvailable()) {
					this.instancesWithAvailableResources.put(instanceToUse.getTaskManagerID(), instanceToUse);
				}

				if (sharedSlot != null) {
					// add the shared slot to the assignment group and allocate a sub-slot
					SimpleSlot slot = constraint == null ?
							groupAssignment.addSharedSlotAndAllocateSubSlot(sharedSlot, locality, groupID) :
							groupAssignment.addSharedSlotAndAllocateSubSlot(sharedSlot, locality, constraint);

					if (slot != null) {
						return slot;
					}
					else {
						// could not add and allocate the sub-slot, so release shared slot
						sharedSlot.releaseSlot(new FlinkException("Could not allocate sub-slot."));
					}
				}
			}
			catch (InstanceDiedException e) {
				// the instance died it has not yet been propagated to this scheduler
				// remove the instance from the set of available instances
				removeInstance(instanceToUse);
			}

			// if we failed to get a slot, fall through the loop
		}
	}