def set_features=(features_json)
      # return unless features_json.class == Hash
      features_json.keys.each do |feature_key|
        # TODO - create feature_key if its missing
        if features_json[feature_key] == "true" || features_json[feature_key] == true
          features.find_or_create_by( feature_key: feature_key)
        else
          features.where( feature_key: feature_key).delete_all
        end
      end
    end