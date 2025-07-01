function (node, oScope) {
				/**
				 * Here we white list all controls that can contain DOM elements with style different than the framework style
				 */
				var skipParents = ["sap.ui.core.HTML"],
					parentNode = jQuery(node).control()[0];

				if (!parentNode) {
					return false;
				}

				var parentName = parentNode.getMetadata().getName(),
					isParentOutOfSkipList = skipParents.indexOf(parentName) === -1,
					isParentInScope = oScope.getElements().indexOf(parentNode) > -1;

				return isParentOutOfSkipList && isParentInScope;

			}