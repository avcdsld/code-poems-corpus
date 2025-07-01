function() {
		this.emit( 'destroy', this );

		for( var i = 0; i < this.tabs.length; i++ ) {
			this.tabs[ i ]._$destroy();
		}
		$( document ).off('mouseup', this.hideAdditionalTabsDropdown);
		this.element.remove();
	}