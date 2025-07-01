function(editor, syntax, profile) {
			var info = editorUtils.outputInfo(editor, syntax, profile);
			if (!~cssSyntaxes.indexOf(info.syntax)) {
				return false;
			}
			
			// let's see if we are expanding gradient definition
			var caret = editor.getCaretPos();
			var content = info.content;
			var gradients = this.gradientsFromCSSProperty(content, caret);
			if (gradients) {
				if (!isValidCaretPosition(gradients, caret, info.syntax)) {
					return false;
				}

				var cssProperty = gradients.property;
				var cssRule = cssProperty.parent;
				var ruleStart = cssRule.options.offset || 0;
				var ruleEnd = ruleStart + cssRule.toString().length;
				
				// Handle special case:
				// user wrote gradient definition between existing CSS 
				// properties and did not finished it with semicolon.
				// In this case, we have semicolon right after gradient 
				// definition and re-parse rule again
				if (/[\n\r]/.test(cssProperty.value())) {
					// insert semicolon at the end of gradient definition
					var insertPos = cssProperty.valueRange(true).start + utils.last(gradients.gradients).matchedPart.end;
					content = utils.replaceSubstring(content, ';', insertPos);
					
					var _gradients = this.gradientsFromCSSProperty(content, caret);
					if (_gradients) {
						gradients = _gradients;
						cssProperty = gradients.property;
						cssRule = cssProperty.parent;
					}
				}
				
				// make sure current property has terminating semicolon
				cssProperty.end(';');
				
				// resolve CSS property name
				var resolvedName = resolvePropertyName(cssProperty.name(), syntax);
				if (resolvedName) {
					cssProperty.name(resolvedName);
				}
				
				pasteGradient(cssProperty, gradients.gradients);
				editor.replaceContent(cssRule.toString(), ruleStart, ruleEnd, true);
				return true;
			}
			
			return this.expandGradientOutsideValue(editor, syntax);
		}