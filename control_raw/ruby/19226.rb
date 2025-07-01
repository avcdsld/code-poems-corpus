def remove_included_asset_group(asset_group_id)
      validate_asset_group(asset_group_id)
      @included_scan_targets[:asset_groups].reject! { |t| t.eql? asset_group_id.to_i }
    end