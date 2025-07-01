def evaluate_subscription(record, field, default, *args)
        default ? record.blank? || record.send(field, *args) : record.present? && record.send(field, *args)
      end