def blob_at(revision, path)
      tree = Rugged::Commit.lookup(self, revision).tree
      begin
        blob_data = tree.path(path)
      rescue Rugged::TreeError
        return nil
      end
      blob = Rugged::Blob.lookup(self, blob_data[:oid])
      (blob.type == :blob) ? blob : nil
    end