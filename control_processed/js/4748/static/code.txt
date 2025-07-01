function () {
            if (!newNodeMap[oldChild.tagID]) {
                // We can finalize existing edits relative to this node *before* it's
                // deleted.
                finalizeNewEdits(oldChild.tagID, true);

                newEdit = {
                    type: "elementDelete",
                    tagID: oldChild.tagID
                };
                newEdits.push(newEdit);

                // deleted element means we need to move on to compare the next
                // of the old tree with the one from the current tree that we
                // just compared
                oldIndex++;
                return true;
            }
            return false;
        }