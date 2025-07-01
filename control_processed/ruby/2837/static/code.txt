def csp_report_only=(new_csp)
      case new_csp
      when OPT_OUT
        @csp_report_only = new_csp
      when ContentSecurityPolicyReportOnlyConfig
        @csp_report_only = new_csp.dup
      when ContentSecurityPolicyConfig
        @csp_report_only = new_csp.make_report_only
      when Hash
        @csp_report_only = ContentSecurityPolicyReportOnlyConfig.new(new_csp)
      else
        raise ArgumentError, "Must provide either an existing CSP config or a CSP config hash"
      end
    end