function(e) {
			this.iterate(false, false, e.shiftKey, true);
			if(!this._ctrlKeyOn(e) && !e.shiftKey){
				this.setSelection(this.currentModel(), false, true);
			}
			e.preventDefault();
			return false;
		}