function( json ) {

		if( json.type === undefined ) {

			throw new Error( "track type undefined, can not parse" );

		}

		var trackType = THREE.KeyframeTrack._getTrackTypeForValueTypeName( json.type );

		if ( json.times === undefined ) {

			var times = [], values = [];

			THREE.AnimationUtils.flattenJSON( json.keys, times, values, 'value' );

			json.times = times;
			json.values = values;

		}

		// derived classes can define a static parse method
		if ( trackType.parse !== undefined ) {

			return trackType.parse( json );

		} else {

			// by default, we asssume a constructor compatible with the base
			return new trackType(
					json.name, json.times, json.values, json.interpolation );

		}

	}