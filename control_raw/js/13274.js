function( nextProps, nextState ) {
		this._container.setState( nextState );
		this._originalComponentWillUpdate.call( this._reactComponent, nextProps, nextState );
	}