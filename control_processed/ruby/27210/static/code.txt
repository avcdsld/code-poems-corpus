def ec_png
      if not cookies[Evercookie.cookie_png].present?
        render :nothing => true, :status => 304
        return true
      end

      response.headers["Content-Type"] = "image/png"
      response.headers["Last-Modified"] = "Wed, 30 Jun 2010 21:36:48 GMT"
      response.headers["Expires"] = "Tue, 31 Dec 2030 23:30:45 GMT"
      response.headers["Cache-Control"] = "private, max-age=630720000"

      render text: get_blob_png, status: 200, content_type: 'image/png'
    end