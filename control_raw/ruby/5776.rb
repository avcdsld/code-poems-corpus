def page_execute_form(params)
      params = prepare_params(params)

      html = %Q(<form id='alipaysubmit' name='alipaysubmit' action='#{@url}' method='POST'>)
      params.each do |key, value|
        html << %Q(<input type='hidden' name='#{key}' value='#{value.gsub("'", "&apos;")}'/>)
      end
      html << "<input type='submit' value='ok' style='display:none'></form>"
      html << "<script>document.forms['alipaysubmit'].submit();</script>"
      html
    end