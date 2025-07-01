def load(uri)
      unloaded = UnloadedAsset.new(uri, self)
      if unloaded.params.key?(:id)
        unless asset = asset_from_cache(unloaded.asset_key)
          id = unloaded.params.delete(:id)
          uri_without_id = build_asset_uri(unloaded.filename, unloaded.params)
          asset = load_from_unloaded(UnloadedAsset.new(uri_without_id, self))
          if asset[:id] != id
            @logger.warn "Sprockets load error: Tried to find #{uri}, but latest was id #{asset[:id]}"
          end
        end
      else
        asset = fetch_asset_from_dependency_cache(unloaded) do |paths|
          # When asset is previously generated, its "dependencies" are stored in the cache.
          # The presence of `paths` indicates dependencies were stored.
          # We can check to see if the dependencies have not changed by "resolving" them and
          # generating a digest key from the resolved entries. If this digest key has not
          # changed, the asset will be pulled from cache.
          #
          # If this `paths` is present but the cache returns nothing then `fetch_asset_from_dependency_cache`
          # will confusingly be called again with `paths` set to nil where the asset will be
          # loaded from disk.
          if paths
            digest = DigestUtils.digest(resolve_dependencies(paths))
            if uri_from_cache = cache.get(unloaded.digest_key(digest), true)
              asset_from_cache(UnloadedAsset.new(uri_from_cache, self).asset_key)
            end
          else
            load_from_unloaded(unloaded)
          end
        end
      end
      Asset.new(asset)
    end