def update_doc(doc_id, params = {}, update_limit = 10)
      resp = {'ok' => false}
      last_fail = nil

      until resp['ok'] or update_limit <= 0
        doc = self.get(doc_id, params)
        yield doc
        begin
          resp = self.save_doc doc
        rescue CouchRest::RequestFailed => e
          if e.http_code == 409 # Update collision
            update_limit -= 1
            last_fail = e
          else
            raise e
          end
        end
      end

      raise last_fail unless resp['ok']
      doc
    end