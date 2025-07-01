function PacketGossipHello(properties) {
			if (properties)
				for (var keys = Object.keys(properties), i = 0; i < keys.length; ++i)
					if (properties[keys[i]] != null)
						this[keys[i]] = properties[keys[i]];
		}