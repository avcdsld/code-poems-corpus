function() {
		var t = this;
		var play = document.createElement('div');
		play.className = 'zy_playpause_btn zy_play';
		t.controls.appendChild(play);
		play.addEventListener('click', function() {
			t.media.isUserClick = true;

			if (t.media.paused) {
				t.media.play();
				// Controls bar auto hide after 3s
				if (!t.media.paused && !t.options.alwaysShowControls) {
					t.setControlsTimer(3000)
				}
			} else {
				t.media.pause()
			}
		});

		function togglePlayPause(s) {
			if (t.media.isUserClick || t.options.autoplay) {
				if ('play' === s) {
					_removeClass(play, 'zy_play');
					_addClass(play, 'zy_pause')
				} else {
					_removeClass(play, 'zy_pause');
					_addClass(play, 'zy_play')
				}
			}
		};

		t.media.addEventListener('play', function() {
			togglePlayPause('play')
		});

		t.media.addEventListener('playing', function() {
			togglePlayPause('play')
		});

		t.media.addEventListener('pause', function() {
			togglePlayPause('pse')
		});

		t.media.addEventListener('paused', function() {
			togglePlayPause('pse')
		});
	}