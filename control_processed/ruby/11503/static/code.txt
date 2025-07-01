def do_add_existing
      parent_record = nested_parent_record(:update)
      @record = active_scaffold_config.model.find(params[:associated_id])
      if parent_record && @record
        parent_record.send(nested.association.name) << @record
        parent_record.save
      else
        false
      end
    end