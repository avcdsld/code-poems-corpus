def add_included_hook
      with_hook_context do |context|
        mod.define_singleton_method :included do |object|
          Builder.pending << object unless context.finalize?
          context.modules.each { |mod| object.send(:include, mod) }
          object.define_singleton_method(:attribute, context.attribute_method)
        end
      end
    end