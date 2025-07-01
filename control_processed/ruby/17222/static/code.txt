def to_representor_hash
      media = @target.is_a?(Hash) ? @target : JSON.parse(@target)
      builder_add_from_deserialized(RepresentorBuilder.new, media).to_representor_hash
    end