function( contentItem, index ) {
		if ( index === undefined ) {
			index = this.contentItems.length;
		}

		this.contentItems.splice( index, 0, contentItem );

		if( this.config.content === undefined ) {
			this.config.content = [];
		}

		this.config.content.splice( index, 0, contentItem.config );
		contentItem.parent = this;
	}