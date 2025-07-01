def record_serializer(rec, nice = true)
      [:messages, :params].each do |key|
        if msgs = rec[key]
          msgs.each do |i, j|
            msgs[i] = (true == nice ? nice_serialize_object(j) : j.inspect)
          end
        end
      end
    end