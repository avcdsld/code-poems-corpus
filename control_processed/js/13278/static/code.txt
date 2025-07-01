function( contentItem, keepChild ) {
		var removedItemSize = contentItem.config[ this._dimension ],
			index = lm.utils.indexOf( contentItem, this.contentItems ),
			splitterIndex = Math.max( index - 1, 0 ),
			i,
			childItem;

		if( index === -1 ) {
			throw new Error( 'Can\'t remove child. ContentItem is not child of this Row or Column' );
		}

		/**
		 * Remove the splitter before the item or after if the item happens
		 * to be the first in the row/column
		 */
		if( this._splitter[ splitterIndex ] ) {
			this._splitter[ splitterIndex ]._$destroy();
			this._splitter.splice( splitterIndex, 1 );
		}

		if( splitterIndex < this._splitter.length ) {
			if ( this._isDocked( splitterIndex ) )
				this._splitter[ splitterIndex ].element.hide();
		}
		/**
		 * Allocate the space that the removed item occupied to the remaining items
		 */
		var docked = this._isDocked();
		for( i = 0; i < this.contentItems.length; i++ ) {
			if( this.contentItems[ i ] !== contentItem ) {
				if ( !this._isDocked( i ) )
					this.contentItems[ i ].config[ this._dimension ] += removedItemSize / ( this.contentItems.length - 1 - docked );
			}
		}

		lm.items.AbstractContentItem.prototype.removeChild.call( this, contentItem, keepChild );

		if( this.contentItems.length === 1 && this.config.isClosable === true ) {
			childItem = this.contentItems[ 0 ];
			this.contentItems = [];
			this.parent.replaceChild( this, childItem, true );
			this._validateDocking( this.parent );
		} else {
			this.callDownwards( 'setSize' );
			this.emitBubblingEvent( 'stateChanged' );
			this._validateDocking();
		}
	}