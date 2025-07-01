def save_doc(doc, bulk = false, batch = false)
      if doc['_attachments']
        doc['_attachments'] = encode_attachments(doc['_attachments'])
      end

      if bulk
        @bulk_save_cache << doc
        bulk_save if @bulk_save_cache.length >= @bulk_save_cache_limit
        return {'ok' => true} # Compatibility with Document#save
      elsif !bulk && @bulk_save_cache.length > 0
        bulk_save
      end
      result = if doc['_id']
        slug = escape_docid(doc['_id'])
        begin
          doc_path = "#{path}/#{slug}"
          doc_path << "?batch=ok" if batch
          connection.put doc_path, doc
        rescue CouchRest::NotFound
          puts "resource not found when saving even though an id was passed"
          slug = doc['_id'] = server.next_uuid
          connection.put "#{path}/#{slug}", doc
        end
      else
        slug = doc['_id'] = @server.next_uuid
        connection.put "#{path}/#{slug}", doc
      end
      if result['ok']
        doc['_id'] = result['id']
        doc['_rev'] = result['rev']
        doc.database = self if doc.respond_to?(:database=)
      end
      result
    end