def reindex(relation, method_name, scoped:, full: false, scope: nil, **options)
      refresh = options.fetch(:refresh, !scoped)

      if method_name
        # update
        import_scope(relation, method_name: method_name, scope: scope)
        self.refresh if refresh
        true
      elsif scoped && !full
        # reindex association
        import_scope(relation, scope: scope)
        self.refresh if refresh
        true
      else
        # full reindex
        reindex_scope(relation, scope: scope, **options)
      end
    end