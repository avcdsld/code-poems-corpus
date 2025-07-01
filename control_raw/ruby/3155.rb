def append_label(solr_doc, solr_field_key, field_info, val)
        ActiveFedora::Indexing::Inserter.create_and_insert_terms(solr_field_key,
                                                                 val,
                                                                 field_info.behaviors, solr_doc)
        ActiveFedora::Indexing::Inserter.create_and_insert_terms("#{solr_field_key}_label",
                                                                 val,
                                                                 field_info.behaviors, solr_doc)
      end