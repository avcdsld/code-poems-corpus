def find_or_create_forum(category_name, forum_name, options={ })
      category = self.find_or_create_category(category_name, options)
      if category
        self.forums.detect { |f| f['category_id'] == category['id'] && f['name'] == forum_name } || post_forum(category['id'], forum_name)
      end
    end