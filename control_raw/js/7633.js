function reject(vReason) {
			vResult = vReason;
			iState = -1;

			if (!bCaught && SyncPromise.listener) {
				SyncPromise.listener(that, false);
			}

			if (fnReject) {
				fnReject(vReason);
				fnReject = fnResolve = null; // be nice to the garbage collector
			}
		}