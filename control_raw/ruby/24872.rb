def query?(name_sym, rpc_desc)
      name_sym.to_s.start_with?('get') ||
        rpc_desc.rpc_desc.input == Google::Protobuf::Empty
    end