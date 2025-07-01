function(ctx, flag) {
				// ctx.node.debug("nodeSetFocus(" + flag + ")");
				var ctx2,
					tree = ctx.tree,
					node = ctx.node,
					opts = tree.options,
					// et = ctx.originalEvent && ctx.originalEvent.type,
					isInput = ctx.originalEvent
						? $(ctx.originalEvent.target).is(":input")
						: false;

				flag = flag !== false;

				// (node || tree).debug("nodeSetFocus(" + flag + "), event: " + et + ", isInput: "+ isInput);
				// Blur previous node if any
				if (tree.focusNode) {
					if (tree.focusNode === node && flag) {
						// node.debug("nodeSetFocus(" + flag + "): nothing to do");
						return;
					}
					ctx2 = $.extend({}, ctx, { node: tree.focusNode });
					tree.focusNode = null;
					this._triggerNodeEvent("blur", ctx2);
					this._callHook("nodeRenderStatus", ctx2);
				}
				// Set focus to container and node
				if (flag) {
					if (!this.hasFocus()) {
						node.debug("nodeSetFocus: forcing container focus");
						this._callHook("treeSetFocus", ctx, true, {
							calledByNode: true,
						});
					}
					node.makeVisible({ scrollIntoView: false });
					tree.focusNode = node;
					if (opts.titlesTabbable) {
						if (!isInput) {
							// #621
							$(node.span)
								.find(".fancytree-title")
								.focus();
						}
					} else {
						// We cannot set KB focus to a node, so use the tree container
						// #563, #570: IE scrolls on every call to .focus(), if the container
						// is partially outside the viewport. So do it only, when absolutely
						// neccessary:
						if (
							$(document.activeElement).closest(
								".fancytree-container"
							).length === 0
						) {
							$(tree.$container).focus();
						}
					}
					if (opts.aria) {
						// Set active descendant to node's span ID (create one, if needed)
						$(tree.$container).attr(
							"aria-activedescendant",
							$(node.tr || node.li)
								.uniqueId()
								.attr("id")
						);
						// "ftal_" + opts.idPrefix + node.key);
					}
					// $(node.span).find(".fancytree-title").focus();
					this._triggerNodeEvent("focus", ctx);
					// if( opts.autoActivate ){
					// 	tree.nodeSetActive(ctx, true);
					// }
					if (opts.autoScroll) {
						node.scrollIntoView();
					}
					this._callHook("nodeRenderStatus", ctx);
				}
			}