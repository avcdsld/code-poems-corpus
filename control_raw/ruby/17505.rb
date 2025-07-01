def to_xml_for_invoice_messages(b = Builder::XmlMarkup.new)
      b.TrackingCategory {
        b.TrackingCategoryID self.tracking_category_id unless tracking_category_id.nil?
        b.Name self.name
        b.Option self.options.is_a?(Array) ? self.options.first : self.options.to_s
      }
    end