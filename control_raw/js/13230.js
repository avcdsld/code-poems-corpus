function( root ) {
		var config, next, i;

		if( this.isInitialised === false ) {
			throw new Error( 'Can\'t create config, layout not yet initialised' );
		}

		if( root && !( root instanceof lm.items.AbstractContentItem ) ) {
			throw new Error( 'Root must be a ContentItem' );
		}

		/*
		 * settings & labels
		 */
		config = {
			settings: lm.utils.copy( {}, this.config.settings ),
			dimensions: lm.utils.copy( {}, this.config.dimensions ),
			labels: lm.utils.copy( {}, this.config.labels )
		};

		/*
		 * Content
		 */
		config.content = [];
		next = function( configNode, item ) {
			var key, i;

			for( key in item.config ) {
				if( key !== 'content' ) {
					configNode[ key ] = item.config[ key ];
				}
			}

			if( item.contentItems.length ) {
				configNode.content = [];

				for( i = 0; i < item.contentItems.length; i++ ) {
					configNode.content[ i ] = {};
					next( configNode.content[ i ], item.contentItems[ i ] );
				}
			}
		};

		if( root ) {
			next( config, { contentItems: [ root ] } );
		} else {
			next( config, this.root );
		}

		/*
		 * Retrieve config for subwindows
		 */
		this._$reconcilePopoutWindows();
		config.openPopouts = [];
		for( i = 0; i < this.openPopouts.length; i++ ) {
			config.openPopouts.push( this.openPopouts[ i ].toConfig() );
		}

		/*
		 * Add maximised item
		 */
		config.maximisedItemId = this._maximisedItem ? '__glMaximised' : null;
		return config;
	}