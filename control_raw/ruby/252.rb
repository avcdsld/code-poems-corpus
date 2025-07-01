def serializable_add_includes(options = {}) #:nodoc:
        return unless includes = options[:include]

        unless includes.is_a?(Hash)
          includes = Hash[Array(includes).flat_map { |n| n.is_a?(Hash) ? n.to_a : [[n, {}]] }]
        end

        includes.each do |association, opts|
          if records = send(association)
            yield association, records, opts
          end
        end
      end