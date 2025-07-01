def read_uint8(data: nil, stream: nil, offset: 0)
      _read_fixint(name: :uint8,    length: 1, pack_format: PACK_FORMAT_UINT8,    data: data, stream: stream, offset: offset)
    end