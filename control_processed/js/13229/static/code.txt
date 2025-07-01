function( contentItem ) {

		/*
		 * The item was dropped on the header area. Just add it as a child of this stack and
		 * get the hell out of this logic
		 */
		if( this._dropSegment === 'header' ) {
			this._resetHeaderDropZone();
			this.addChild( contentItem, this._dropIndex );
			return;
		}

		/*
		 * The item was dropped on the top-, left-, bottom- or right- part of the content. Let's
		 * aggregate some conditions to make the if statements later on more readable
		 */
		var isVertical = this._dropSegment === 'top' || this._dropSegment === 'bottom',
			isHorizontal = this._dropSegment === 'left' || this._dropSegment === 'right',
			insertBefore = this._dropSegment === 'top' || this._dropSegment === 'left',
			hasCorrectParent = ( isVertical && this.parent.isColumn ) || ( isHorizontal && this.parent.isRow ),
			type = isVertical ? 'column' : 'row',
			dimension = isVertical ? 'height' : 'width',
			index,
			stack,
			rowOrColumn;

		/*
		 * The content item can be either a component or a stack. If it is a component, wrap it into a stack
		 */
		if( contentItem.isComponent ) {
			stack = this.layoutManager.createContentItem({ type: 'stack' }, this );
			stack.addChild( contentItem );
			contentItem = stack;
		}

		/*
		 * If the item is dropped on top or bottom of a column or left and right of a row, it's already
		 * layd out in the correct way. Just add it as a child
		 */
		if( hasCorrectParent ) {
			index = lm.utils.indexOf( this, this.parent.contentItems );
			this.parent.addChild( contentItem, insertBefore ? index : index + 1, true );
			this.config[ dimension ] *= 0.5;
			contentItem.config[ dimension ] = this.config[ dimension ];
			this.parent.callDownwards( 'setSize' );
		/*
		 * This handles items that are dropped on top or bottom of a row or left / right of a column. We need
		 * to create the appropriate contentItem for them to life in
		 */
		} else {
			type = isVertical ? 'column' : 'row';
			rowOrColumn = this.layoutManager.createContentItem({ type: type }, this );
			this.parent.replaceChild( this, rowOrColumn );

			rowOrColumn.addChild( contentItem, insertBefore ? 0 : undefined, true );
			rowOrColumn.addChild( this, insertBefore ? undefined : 0, true );

			this[ dimension ] = 50;
			contentItem[ dimension ] = 50;
			rowOrColumn.callDownwards( 'setSize' );
		}
	}