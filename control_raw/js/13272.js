function(component) {
		this._reactComponent = component;
		this._originalComponentWillUpdate = this._reactComponent.componentWillUpdate || function() {};
		this._reactComponent.componentWillUpdate = this._onUpdate.bind( this );
		if( this._container.getState() ) {
			this._reactComponent.setState( this._container.getState() );
		}
	}