def render_hashes(tags, **opts)
      meta_tags.meta_tags.each_key do |property|
        render_hash(tags, property, **opts)
      end
    end