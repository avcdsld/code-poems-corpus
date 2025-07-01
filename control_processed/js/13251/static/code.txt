function( e ) {
		e && e.preventDefault();
		if( this.isMaximised === true ) {
			this.layoutManager._$minimiseItem( this );
		} else {
			this.layoutManager._$maximiseItem( this );
		}

		this.isMaximised = !this.isMaximised;
		this.emitBubblingEvent( 'stateChanged' );
	}