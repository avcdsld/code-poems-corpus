def update_contents(contents_attributes)
      return true if contents_attributes.nil?
      contents.each do |content|
        content_hash = contents_attributes[content.id.to_s] || next
        content.update_essence(content_hash) || errors.add(:base, :essence_validation_failed)
      end
      errors.blank?
    end