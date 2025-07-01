def perform_action!(action, resource, author, extra_log_info = {})
      PaperTrail.request(whodunnit: gid(author)) do
        Decidim::ApplicationRecord.transaction do
          result = block_given? ? yield : nil
          loggable_resource = resource.is_a?(Class) ? result : resource
          log(action, author, loggable_resource, extra_log_info)
          return result
        end
      end
    end