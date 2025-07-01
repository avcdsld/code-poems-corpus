function( filter ) {
		var result = [],
			next = function( contentItem ) {
				for( var i = 0; i < contentItem.contentItems.length; i++ ) {
					
					if( filter( contentItem.contentItems[ i ] ) === true ) {
						result.push( contentItem.contentItems[ i ] );
					}

					next( contentItem.contentItems[ i ] );
				}
			};

		next( this );
		return result;
	}