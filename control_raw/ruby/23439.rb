def solve_conflict(connec_entity, external_entities, external_entity_name, idmap, id_refs_only_connec_entity)
      # Here the connec_entity['id'] is an external id (String) because the entity has been unfolded.
      external_entity = external_entities.find { |entity| connec_entity['id'] == @current_entity.class.id_from_external_entity_hash(entity) }
      # No conflict
      return map_connec_entity_with_idmap(connec_entity, external_entity_name, idmap, id_refs_only_connec_entity) unless external_entity

      # Conflict
      # We keep the most recently updated entity
      keep_connec = @opts.key?(:connec_preemption) ? @opts[:connec_preemption] : connec_more_recent?(connec_entity, external_entity)

      if keep_connec
        Maestrano::Connector::Rails::ConnectorLogger.log('info', @organization, "Conflict between #{Maestrano::Connector::Rails::External.external_name} #{external_entity_name} #{external_entity} and Connec! #{@current_entity.class.connec_entity_name} #{connec_entity}. Entity from Connec! kept")
        external_entities.delete(external_entity)
        map_connec_entity_with_idmap(connec_entity, external_entity_name, idmap, id_refs_only_connec_entity)
      else
        Maestrano::Connector::Rails::ConnectorLogger.log('info', @organization, "Conflict between #{Maestrano::Connector::Rails::External.external_name} #{external_entity_name} #{external_entity} and Connec! #{@current_entity.class.connec_entity_name} #{connec_entity}. Entity from external kept")
        nil
      end
    end