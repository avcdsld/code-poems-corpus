def linked_classes_for(klass)
      return [] unless klass.respond_to?(:linked_classes_for)

      klass.linked_classes_for(current_component).map do |k|
        [k.underscore, t(k.demodulize.underscore, scope: "decidim.filters.linked_classes")]
      end
    end