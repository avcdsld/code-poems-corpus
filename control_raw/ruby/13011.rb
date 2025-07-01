def author_names_and_newness_for_thread t, limit=nil
    new = {}
    seen = {}
    authors = t.map do |m, *o|
      next unless m && m.from
      new[m.from] ||= m.has_label?(:unread)
      next if seen[m.from]
      seen[m.from] = true
      m.from
    end.compact

    result = []
    authors.each do |a|
      break if limit && result.size >= limit
      name = if AccountManager.is_account?(a)
        "me"
      elsif t.authors.size == 1
        a.mediumname
      else
        a.shortname
      end

      result << [name, new[a]]
    end

    if result.size == 1 && (author_and_newness = result.assoc("me"))
      unless (recipients = t.participants - t.authors).empty?
        result = recipients.collect do |r|
          break if limit && result.size >= limit
          name = (recipients.size == 1) ? r.mediumname : r.shortname
          ["(#{name})", author_and_newness[1]]
        end
      end
    end

    result
  end