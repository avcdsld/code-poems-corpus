def render_links(tags)
      [ :amphtml, :canonical, :prev, :next, :image_src ].each do |tag_name|
        href = meta_tags.extract(tag_name)
        if href.present?
          @normalized_meta_tags[tag_name] = href
          tags << Tag.new(:link, rel: tag_name, href: href)
        end
      end
    end