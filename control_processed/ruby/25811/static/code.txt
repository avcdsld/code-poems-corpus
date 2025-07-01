def create
      pfid = begin
        self.product_family_id
      rescue NoMethodError
        0
      end
      connection.post("/product_families/#{pfid}/products.#{self.class.format.extension}", encode, self.class.headers).tap do |response|
        self.id = id_from_response(response)
        load_attributes_from_response(response)
      end
    end