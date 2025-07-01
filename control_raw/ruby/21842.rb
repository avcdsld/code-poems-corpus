def _parse_no_rotate_params(hash, params, line)
      sym = (line.include? 'symmetric') ? true : false

      select_hash = params[1]
      lparams = select_hash.split('-')
      if lparams[0].downcase == 'destination'
        bselect = 'dst'
        bhash = lparams[1]
        # there are bundles hashes like ip-gre which
        # need extra processing
        bhash += '-gre' if select_hash.include? 'gre'
      else
        if select_hash.include? '-dest-'
          bselect = 'src-dst'
          bhash = lparams[2]
          bhash += '-gre' if select_hash.include? 'gre'
          # there are bundles hashes like ip-only and
          # port-only specific to src-dst
          bhash += '-only' if select_hash.include? 'only'
        else
          bselect = 'src'
          bhash = lparams[1]
          # there are bundles hashes like ip-gre which
          # need extra processing
          bhash += '-gre' if select_hash.include? 'gre'
        end
      end
      hash[:bundle_select] = bselect
      hash[:bundle_hash] = bhash
      hash[:symmetry] = sym
      hash
    end