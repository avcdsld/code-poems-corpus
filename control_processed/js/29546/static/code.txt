function KeyStroke (keyCode, mod1, mod2, mod3, mod4, type) {
		this.type = type || "keydown"; //$NON-NLS-0$
		if (typeof(keyCode) === "string" && this.type === "keydown") { //$NON-NLS-1$ //$NON-NLS-0$
			this.keyCode = keyCode.toUpperCase().charCodeAt(0);
		} else {
			this.keyCode = keyCode;
		}
		this.mod1 = mod1 !== undefined && mod1 !== null ? mod1 : false;
		this.mod2 = mod2 !== undefined && mod2 !== null ? mod2 : false;
		this.mod3 = mod3 !== undefined && mod3 !== null ? mod3 : false;
		this.mod4 = mod4 !== undefined && mod4 !== null ? mod4 : false;
	}