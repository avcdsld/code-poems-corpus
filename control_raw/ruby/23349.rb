def sort_items_according_to_current_direction
      case @direction
      when nil
        @items = items.shift(2) + items.partition(&:directory?).flat_map(&:sort)
      when 'r'
        @items = items.shift(2) + items.partition(&:directory?).flat_map {|arr| arr.sort.reverse}
      when 'S', 's'
        @items = items.shift(2) + items.partition(&:directory?).flat_map {|arr| arr.sort_by {|i| -i.size}}
      when 'Sr', 'sr'
        @items = items.shift(2) + items.partition(&:directory?).flat_map {|arr| arr.sort_by(&:size)}
      when 't'
        @items = items.shift(2) + items.partition(&:directory?).flat_map {|arr| arr.sort {|x, y| y.mtime <=> x.mtime}}
      when 'tr'
        @items = items.shift(2) + items.partition(&:directory?).flat_map {|arr| arr.sort_by(&:mtime)}
      when 'c'
        @items = items.shift(2) + items.partition(&:directory?).flat_map {|arr| arr.sort {|x, y| y.ctime <=> x.ctime}}
      when 'cr'
        @items = items.shift(2) + items.partition(&:directory?).flat_map {|arr| arr.sort_by(&:ctime)}
      when 'u'
        @items = items.shift(2) + items.partition(&:directory?).flat_map {|arr| arr.sort {|x, y| y.atime <=> x.atime}}
      when 'ur'
        @items = items.shift(2) + items.partition(&:directory?).flat_map {|arr| arr.sort_by(&:atime)}
      when 'e'
        @items = items.shift(2) + items.partition(&:directory?).flat_map {|arr| arr.sort {|x, y| y.extname <=> x.extname}}
      when 'er'
        @items = items.shift(2) + items.partition(&:directory?).flat_map {|arr| arr.sort_by(&:extname)}
      end
      items.each.with_index {|item, index| item.index = index}
    end