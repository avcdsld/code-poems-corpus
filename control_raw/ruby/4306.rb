def run_targeted_callbacks(place, kind)
      name = "_run__#{place}__#{kind}__callbacks"
      unless respond_to?(name)
        chain = ActiveSupport::Callbacks::CallbackChain.new(name, {})
        send("_#{kind}_callbacks").each do |callback|
          chain.append(callback) if callback.kind == place
        end
        self.class.send :define_method, name do
          env = ActiveSupport::Callbacks::Filters::Environment.new(self, false, nil)
          sequence = chain.compile
          sequence.invoke_before(env)
          env.value = !env.halted
          sequence.invoke_after(env)
          env.value
        end
        self.class.send :protected, name
      end
      send(name)
    end