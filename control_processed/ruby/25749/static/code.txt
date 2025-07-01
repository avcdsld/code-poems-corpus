def resize(prefix_len)
			m32 = Mask32.new(prefix_len)
			return IPv4Net.new(self.network,m32)
		end