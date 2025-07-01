def validate(record)
      if record._database_validations_fallback
        super
      else
        return unless record.public_send(foreign_key).blank? && record.public_send(association).blank?

        record.errors.add(association, :blank, message: BelongsToOptions::VALIDATOR_MESSAGE)
      end
    end