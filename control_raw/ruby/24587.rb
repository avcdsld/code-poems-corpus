def standard_address(network: nil)
      if public_key_hash_script?
        return BTC::PublicKeyAddress.new(hash: @chunks[2].pushdata, network: network)
      elsif script_hash_script?
        return BTC::ScriptHashAddress.new(hash: @chunks[1].pushdata, network: network)
      elsif public_key_script?
        return BTC::PublicKeyAddress.new(hash: BTC.hash160(@chunks[0].pushdata), network: network)
      end
      nil
    end