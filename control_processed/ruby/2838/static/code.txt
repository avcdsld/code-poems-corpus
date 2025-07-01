def recaptcha_tags(options = {})
      if options.key?(:stoken)
        raise(RecaptchaError, "Secure Token is deprecated. Please remove 'stoken' from your calls to recaptcha_tags.")
      end
      if options.key?(:ssl)
        raise(RecaptchaError, "SSL is now always true. Please remove 'ssl' from your calls to recaptcha_tags.")
      end

      noscript = options.delete(:noscript)

      html, tag_attributes, fallback_uri = Recaptcha::ClientHelper.recaptcha_components(options)
      html << %(<div #{tag_attributes}></div>\n)

      if noscript != false
        html << <<-HTML
          <noscript>
            <div>
              <div style="width: 302px; height: 422px; position: relative;">
                <div style="width: 302px; height: 422px; position: absolute;">
                  <iframe
                    src="#{fallback_uri}"
                    name="ReCAPTCHA"
                    style="width: 302px; height: 422px; border-style: none; border: 0; overflow: hidden;">
                  </iframe>
                </div>
              </div>
              <div style="width: 300px; height: 60px; border-style: none;
                bottom: 12px; left: 25px; margin: 0px; padding: 0px; right: 25px;
                background: #f9f9f9; border: 1px solid #c1c1c1; border-radius: 3px;">
                <textarea id="g-recaptcha-response" name="g-recaptcha-response"
                  class="g-recaptcha-response"
                  style="width: 250px; height: 40px; border: 1px solid #c1c1c1;
                  margin: 10px 25px; padding: 0px; resize: none;">
                </textarea>
              </div>
            </div>
          </noscript>
        HTML
      end

      html.respond_to?(:html_safe) ? html.html_safe : html
    end