def copy_to(target, opts={})

      counter = 0

      %w[
        configurations errors expressions msgs schedules variables workitems
      ].each do |type|

        ids(type).each do |id|

          item = get(type, id)

          item.delete('_rev')
          target.put(item)

          counter += 1
          puts("  #{type}/#{item['_id']}") if opts[:verbose]
        end
      end

      counter
    end