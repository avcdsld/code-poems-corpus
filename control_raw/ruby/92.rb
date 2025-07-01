def generate(value, expires_at: nil, expires_in: nil, purpose: nil)
      data = encode(Messages::Metadata.wrap(@serializer.dump(value), expires_at: expires_at, expires_in: expires_in, purpose: purpose))
      "#{data}--#{generate_digest(data)}"
    end