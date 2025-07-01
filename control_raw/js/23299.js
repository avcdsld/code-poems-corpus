function(editor, syntax, profile) {
			var newPoint = findNewEditPoint(editor, 1);
			if (newPoint != -1) {
				editor.setCaretPos(newPoint);
				return true;
			}
			
			return false;
		}