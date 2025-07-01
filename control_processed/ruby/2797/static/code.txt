def replace_view(name, version: nil, revert_to_version: nil, materialized: false)
      if version.blank?
        raise ArgumentError, "version is required"
      end

      if materialized
        raise ArgumentError, "Cannot replace materialized views"
      end

      sql_definition = definition(name, version)

      Scenic.database.replace_view(name, sql_definition)
    end