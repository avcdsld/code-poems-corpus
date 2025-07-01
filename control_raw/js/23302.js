function updateImageSizeHTML(editor) {
		var offset = editor.getCaretPos();

		// find tag from current caret position
		var info = editorUtils.outputInfo(editor);
		var xmlElem = xmlEditTree.parseFromPosition(info.content, offset, true);
		if (xmlElem && (xmlElem.name() || '').toLowerCase() == 'img') {
			getImageSizeForSource(editor, xmlElem.value('src'), function(size) {
				if (size) {
					var compoundData = xmlElem.range(true);
					xmlElem.value('width', size.width);
					xmlElem.value('height', size.height, xmlElem.indexOf('width') + 1);

					actionUtils.compoundUpdate(editor, utils.extend(compoundData, {
						data: xmlElem.toString(),
						caret: offset
					}));
				}
			});
		}
	}