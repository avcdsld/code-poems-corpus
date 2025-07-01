def _parse_ethernet_params(hash, params)
      hash_poly = params[2]

      # Depending on the chipset, hash_poly may have have a different
      # default value within the same platform family (this is done to
      # avoid polarization) but there is currently no command available
      # to dynamically determine the default state. As a result the
      # getter simply hard-codes a default value which means it may
      # encounter occasional idempotence issues.
      hash_poly = hash_poly.nil? ? 'CRC10b' : hash_poly

      select_hash = params[1]
      lparams = select_hash.split('-')
      if lparams[0].downcase == 'destination'
        bselect = 'dst'
        bhash = lparams[1]
      else
        if select_hash.include? '-dest-'
          bselect = 'src-dst'
          bhash = lparams[2]
          # there are bundles hashes like ip-only and
          # port-only specific to src-dst
          bhash += '-only' if select_hash.include? 'only'
        else
          bselect = 'src'
          bhash = lparams[1]
        end
      end
      hash[:bundle_select] = bselect
      hash[:bundle_hash] = bhash
      hash[:hash_poly] = hash_poly
      hash
    end