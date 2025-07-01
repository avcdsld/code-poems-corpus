function ( index ) {
		if ( typeof index == 'undefined' ) {
			var count = 0;
			for (var i = 0; i < this.contentItems.length; ++i)
				if ( this._isDocked( i ) )
					count++;
			return count;
		}
		if ( index < this.contentItems.length )
			return this.contentItems[ index ]._docker && this.contentItems[ index ]._docker.docked;
	}