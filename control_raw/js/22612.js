function () {

		var f, fl = this.lensFlares.length;
		var flare;
		var vecX = - this.positionScreen.x * 2;
		var vecY = - this.positionScreen.y * 2;

		for ( f = 0; f < fl; f ++ ) {

			flare = this.lensFlares[ f ];

			flare.x = this.positionScreen.x + vecX * flare.distance;
			flare.y = this.positionScreen.y + vecY * flare.distance;

			flare.wantedRotation = flare.x * Math.PI * 0.25;
			flare.rotation += ( flare.wantedRotation - flare.rotation ) * 0.25;

		}

	}