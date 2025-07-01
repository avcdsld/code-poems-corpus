function( config ) {
		var windowConfigKey = lm.utils.getQueryStringParam( 'gl-window' );

		if( windowConfigKey ) {
			this.isSubWindow = true;
			config = localStorage.getItem( windowConfigKey );
			config = JSON.parse( config );
			config = ( new lm.utils.ConfigMinifier() ).unminifyConfig( config );
			localStorage.removeItem( windowConfigKey );
		}

		config = $.extend( true, {}, lm.config.defaultConfig, config );

		var nextNode = function( node ) {
			for( var key in node ) {
				if( key !== 'props' && typeof node[ key ] === 'object' ) {
					nextNode( node[ key ] );
				}
				else if( key === 'type' && node[ key ] === 'react-component' ) {
					node.type = 'component';
					node.componentName = 'lm-react-component';
				}
			}
		}

		nextNode( config );

		if( config.settings.hasHeaders === false ) {
			config.dimensions.headerHeight = 0;
		}

		return config;
	}