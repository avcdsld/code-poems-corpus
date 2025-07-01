def update_image_sizes(data=nil,generate_objects=false)
            uri = URI.parse(@uri + "/Sizes")
            put(uri,data,generate_objects)
        end