def set_cookie(name, domain, value = "", path = "/", httponly = false, expires = "")
			sig = encode(GrabzIt::Utility.nil_check(@applicationSecret)+"|"+GrabzIt::Utility.nil_check(name)+"|"+GrabzIt::Utility.nil_check(domain)+
			"|"+GrabzIt::Utility.nil_check(value)+"|"+GrabzIt::Utility.nil_check(path)+"|"+GrabzIt::Utility.b_to_str(httponly)+
			"|"+GrabzIt::Utility.nil_check(expires)+"|0")

			qs = "key="
			qs.concat(CGI.escape(GrabzIt::Utility.nil_check(@applicationKey)))
			qs.concat("&domain=")
			qs.concat(CGI.escape(GrabzIt::Utility.nil_check(domain)))
			qs.concat("&name=")
			qs.concat(CGI.escape(GrabzIt::Utility.nil_check(name)))
			qs.concat("&value=")
			qs.concat(CGI.escape(GrabzIt::Utility.nil_check(value)))
			qs.concat("&path=")
			qs.concat(CGI.escape(GrabzIt::Utility.nil_check(path)))
			qs.concat("&httponly=")
			qs.concat(GrabzIt::Utility.b_to_str(httponly))
			qs.concat("&expires=")
			qs.concat(CGI.escape(GrabzIt::Utility.nil_check(expires)))
			qs.concat("&sig=")
			qs.concat(sig)

			return (get_result_value(get(@protocol + WebServicesBaseURLGet + "setcookie.ashx?" + qs), "Result") == TrueString)
		end