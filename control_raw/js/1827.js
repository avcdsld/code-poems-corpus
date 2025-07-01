function() {
		var t = this;
		var timeline = document.createElement('div');
		timeline.className = 'zy_timeline';
		timeline.innerHTML = '<div class="zy_timeline_slider">' +
			'<div class="zy_timeline_buffering" style="display:none"></div>' +
			'<div class="zy_timeline_loaded"></div>' +
			'<div class="zy_timeline_current"></div>' +
			'<div class="zy_timeline_handle"></div>' +
			'</div>';
		t.controls.appendChild(timeline);

		t.slider = timeline.children[0];
		t.buffering = t.slider.children[0];
		t.loaded = t.slider.children[1];
		t.current = t.slider.children[2];
		t.handle = t.slider.children[3];

		var isPointerDown = false;
		var _X = t.slider.offsetLeft;
		var _W = _css(t.slider, 'width');

		var pointerMove = function(e) {
			var _time = 0;
			var x;

			if (e.changedTouches) {
				x = e.changedTouches[0].pageX
			} else {
				x = e.pageX
			}

			if (t.media.duration) {
				if (x < _X) {
					x = _X
				} else if (x > _W + _X) {
					x = _W + _X
				}

				_time = ((x - _X) / _W) * t.media.duration;

				if (isPointerDown && _time !== t.media.currentTime) {
					t.media.currentTime = _time
				}
			}
		};
		// Handle clicks
		if (zyMedia.features.hasTouch) {
			t.slider.addEventListener('touchstart', function(e) {
				isPointerDown = true;
				pointerMove(e);
				_X = t.slider.offsetLeft;
				_W = _css(t.slider, 'width');
				t.slider.addEventListener('touchmove', pointerMove);
				t.slider.addEventListener('touchend', function(e) {
					isPointerDown = false;
					t.slider.removeEventListener('touchmove', pointerMove)
				});
			});
		} else {
			t.slider.addEventListener('mousedown', function(e) {
				isPointerDown = true;
				pointerMove(e);
				_X = t.slider.offsetLeft;
				_W = _css(t.slider, 'width');
				t.slider.addEventListener('mousemove', pointerMove);
				t.slider.addEventListener('mouseup', function(e) {
					isPointerDown = false;
					t.slider.addEventListener('mousemove', pointerMove)
				});
			});
		}

		t.slider.addEventListener('mouseenter', function(e) {
			t.slider.addEventListener('mousemove', pointerMove);
		});

		t.slider.addEventListener('mouseleave', function(e) {
			if (!isPointerDown) {
				t.slider.removeEventListener('mousemove', pointerMove)
			}
		});

		//4Hz ~ 66Hz, no longer than 250ms
		t.media.addEventListener('timeupdate', function(e) {
			t.updateTimeline(e)
		});
	}