function ( divisions ) {

		if ( ! divisions ) divisions = 5;

		var d, pts = [];

		for ( d = 0; d <= divisions; d ++ ) {

			pts.push( this.getPointAt( d / divisions ) );

		}

		return pts;

	}