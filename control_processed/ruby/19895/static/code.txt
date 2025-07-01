def __phpot_decoder(ip)
			octets = ip.split(/\./)
			if octets.length != 4 or octets[0] != "127"
				return "invalid response"
			elsif octets[3] == "0"
				search_engines = ["undocumented", "AltaVista", "Ask", "Baidu", "Excite", "Google", "Looksmart", "Lycos", "MSN", "Yahoo", "Cuil", "InfoSeek", "Miscellaneous"]
				sindex = octets[2].to_i
				if sindex >= search_engines.length
					return "type=search engine,engine=unknown"
				else
					return "type=search engine,engine=#{search_engines[sindex]}"
				end
			else
				days, threatscore, flags = octets[1,3]
				flags = flags.to_i
				types = []
				if (flags & 0x1) == 0x1
					types << "suspicious"
				end
				if (flags & 0x2) == 0x2
					types << "harvester"
				end
				if (flags & 0x4) == 0x4
					types << "comment spammer"
				end
				if (flags & 0xf8) > 0
					types << "reserved"
				end
				type = types.join(",")
				return "days=#{days},score=#{threatscore},type=#{type}"
			end
		end