def title_slug
      value = (@options['slug'] || @options['title']).downcase
      value.gsub!(/[^\x00-\x7F]/u, '')
      value.gsub!(/(&amp;|&)+/, 'and')
      value.gsub!(/[']+/, '')
      value.gsub!(/\W+/, ' ')
      value.strip!
      value.gsub!(' ', '-')
      value
    end