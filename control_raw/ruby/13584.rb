def level_for_item(navi_key)
      return level if self[navi_key]

      items.each do |item|
        next unless item.sub_navigation
        level = item.sub_navigation.level_for_item(navi_key)
        return level if level
      end
      return nil
    end