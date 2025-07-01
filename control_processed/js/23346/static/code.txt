function(editor, filepath) {
			var data = String(editor.getSelection());
			var caretPos = editor.getCaretPos();
			var info = editorUtils.outputInfo(editor);

			if (!data) {
				// no selection, try to find image bounds from current caret position
				var text = info.content, m;
				while (caretPos-- >= 0) {
					if (startsWith('src=', text, caretPos)) { // found <img src="">
						if ((m = text.substr(caretPos).match(/^(src=(["'])?)([^'"<>\s]+)\1?/))) {
							data = m[3];
							caretPos += m[1].length;
						}
						break;
					} else if (startsWith('url(', text, caretPos)) { // found CSS url() pattern
						if ((m = text.substr(caretPos).match(/^(url\((['"])?)([^'"\)\s]+)\1?/))) {
							data = m[3];
							caretPos += m[1].length;
						}
						break;
					}
				}
			}

			if (data) {
				if (startsWith('data:', data)) {
					return decodeFromBase64(editor, filepath, data, caretPos);
				} else {
					return encodeToBase64(editor, data, caretPos);
				}
			}

			return false;
		}