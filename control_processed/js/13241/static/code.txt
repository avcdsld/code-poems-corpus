function() {
		var popInButton = $( '<div class="lm_popin" title="' + this.config.labels.popin + '">' +
			'<div class="lm_icon"></div>' +
			'<div class="lm_bg"></div>' +
			'</div>' );

		popInButton.on( 'click', lm.utils.fnBind( function() {
			this.emit( 'popIn' );
		}, this ) );

		document.title = lm.utils.stripTags( this.config.content[ 0 ].title );

		$( 'head' ).append( $( 'body link, body style, template, .gl_keep' ) );

		this.container = $( 'body' )
			.html( '' )
			.css( 'visibility', 'visible' )
			.append( popInButton );

		/*
		 * This seems a bit pointless, but actually causes a reflow/re-evaluation getting around
		 * slickgrid's "Cannot find stylesheet." bug in chrome
		 */
		var x = document.body.offsetHeight; // jshint ignore:line

		/*
		 * Expose this instance on the window object
		 * to allow the opening window to interact with
		 * it
		 */
		window.__glInstance = this;
	}