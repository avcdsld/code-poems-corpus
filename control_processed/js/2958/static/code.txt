function setAttrs(vnode3, attrs2, ns) {
		for (var key in attrs2) {
			setAttr(vnode3, key, null, attrs2[key], ns)
		}
	}