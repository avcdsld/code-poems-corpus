function () {
            newEdit = {
                type: "textInsert",
                content: newChild.content,
                parentID: newChild.parent.tagID
            };

            // text changes will generally have afterID and beforeID, but we make
            // special note if it's the first child.
            if (textAfterID) {
                newEdit.afterID = textAfterID;
            } else {
                newEdit.firstChild = true;
            }
            newEdits.push(newEdit);

            // The text node is in the new tree, so we move to the next new tree item
            newIndex++;
        }