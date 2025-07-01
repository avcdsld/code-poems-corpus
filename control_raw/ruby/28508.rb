def djatoka_top_left_square_image_tag(rft_id, params={})
      url = djatoka_top_left_square_image_url(rft_id, params)
      image_tag(url, clean_square_image_tag_params(params))
    end