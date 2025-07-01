def context(new_target, &block)
      return new_target unless block
      # this little line is incredibly important; the context is only set on
      # the top-level Layout object.

      # mp "MOTIONKIT CONTEXT is #{new_target} meta: #{new_target.motion_kit_meta}"
      return parent_layout.context(new_target, &block) unless is_parent_layout?

      if new_target.is_a?(Symbol)
        new_target = self.get_view(new_target)
      end

      context_was, parent_was, delegate_was = @context, @parent, @layout_delegate

      prev_should_run = @should_run_deferred
      if @should_run_deferred.nil?
        @should_run_deferred = true
      else
        @should_run_deferred = false
      end
      @parent = MK::Parent.new(context_was)
      @context = new_target
      @context.motion_kit_meta[:delegate] ||= Layout.layout_for(@context.class)
      @layout_delegate = @context.motion_kit_meta[:delegate]
      if @layout_delegate
        @layout_delegate.set_parent_layout(parent_layout)
      end
      yield
      @layout_delegate, @context, @parent = delegate_was, context_was, parent_was
      if @should_run_deferred
        run_deferred(new_target)
      end
      @should_run_deferred = prev_should_run

      new_target
    end