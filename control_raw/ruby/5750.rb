def render_refresh(tags)
      refresh = meta_tags.extract(:refresh)
      tags << Tag.new(:meta, 'http-equiv' => 'refresh', content: refresh.to_s) if refresh.present?
    end