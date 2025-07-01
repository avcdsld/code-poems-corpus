function() {
		var api_url,
			self = this;

		// Create Dom element
		this._el.content_item	= TL.Dom.create("div", "tl-media-item tl-media-iframe tl-media-spotify", this._el.content);

		// Get Media ID
		if (this.data.url.match(/^spotify:track/) || this.data.url.match(/^spotify:album/) || this.data.url.match(/^spotify:user:.+:playlist:/)) {
			this.media_id = this.data.url;
		}

		if (this.data.url.match(/spotify\.com\/track\/(.+)/)) {
			this.media_id = "spotify:track:" + this.data.url.match(/spotify\.com\/track\/(.+)/)[1];
		} else if (this.data.url.match(/spotify\.com\/album\/(.+)/)) {
			this.media_id = "spotify:album:" + this.data.url.match(/spotify\.com\/album\/(.+)/)[1];
		} else if (this.data.url.match(/spotify\.com\/user\/(.+?)\/playlist\/(.+)/)) {
			var user = this.data.url.match(/spotify\.com\/user\/(.+?)\/playlist\/(.+)/)[1];
			var playlist = this.data.url.match(/spotify\.com\/user\/(.+?)\/playlist\/(.+)/)[2];
			this.media_id = "spotify:user:" + user + ":playlist:" + playlist;
		} else if (this.data.url.match(/spotify\.com\/artist\/(.+)/)) {
			var artist = this.data.url.match(/spotify\.com\/artist\/(.+)/)[1];
			this.media_id = "spotify:artist:" + artist;
		}


		if (this.media_id) {
			// API URL
			api_url = "https://embed.spotify.com/?uri=" + this.media_id + "&theme=white&view=coverart";

			this.player = TL.Dom.create("iframe", "tl-media-shadow", this._el.content_item);
			this.player.width 		= "100%";
			this.player.height 		= "100%";
			this.player.frameBorder = "0";
			this.player.src 		= api_url;

			// After Loaded
			this.onLoaded();

		} else {
				this.loadErrorDisplay(this._('spotify_invalid_url'));
		}
	}