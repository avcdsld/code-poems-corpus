def delete_watermark(identifier)
			sig = encode(GrabzIt::Utility.nil_check(@applicationSecret)+"|"+GrabzIt::Utility.nil_check(identifier))

			qs = "key="
			qs.concat(CGI.escape(GrabzIt::Utility.nil_check(@applicationKey)))
			qs.concat("&identifier=")
			qs.concat(CGI.escape(GrabzIt::Utility.nil_check(identifier)))
			qs.concat("&sig=")
			qs.concat(sig)

			return (get_result_value(get(@protocol + WebServicesBaseURLGet + "deletewatermark.ashx?" + qs), "Result") == TrueString)
		end