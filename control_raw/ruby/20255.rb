def delegate_to_model(method, *args, &block)
      model = self.model
      model.send(:with_scope, query) do
        model.send(method, *args, &block)
      end
    end