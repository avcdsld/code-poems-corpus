function convertSlides() {

		var sections = document.querySelectorAll( '[data-markdown]');

		for( var i = 0, len = sections.length; i < len; i++ ) {

			var section = sections[i];

			// Only parse the same slide once
			if( !section.getAttribute( 'data-markdown-parsed' ) ) {

				section.setAttribute( 'data-markdown-parsed', true )

				var notes = section.querySelector( 'aside.notes' );
				var markdown = getMarkdownFromSlide( section );

				section.innerHTML = marked( markdown );
				addAttributes( 	section, section, null, section.getAttribute( 'data-element-attributes' ) ||
								section.parentNode.getAttribute( 'data-element-attributes' ) ||
								DEFAULT_ELEMENT_ATTRIBUTES_SEPARATOR,
								section.getAttribute( 'data-attributes' ) ||
								section.parentNode.getAttribute( 'data-attributes' ) ||
								DEFAULT_SLIDE_ATTRIBUTES_SEPARATOR);

				// If there were notes, we need to re-add them after
				// having overwritten the section's HTML
				if( notes ) {
					section.appendChild( notes );
				}

			}

		}

	}