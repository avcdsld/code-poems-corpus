def buffer_initialize(options={})
      if ! self.class.method_defined?(:flush)
        raise ArgumentError, "Any class including Stud::Buffer must define a flush() method."
      end

      @buffer_config = {
        :max_items => options[:max_items] || 50,
        :max_interval => options[:max_interval] || 5,
        :logger => options[:logger] || nil,
        :autoflush => options.fetch(:autoflush, true),
        :has_on_flush_error => self.class.method_defined?(:on_flush_error),
        :has_on_full_buffer_receive => self.class.method_defined?(:on_full_buffer_receive),
        :drop_messages_on_flush_error => options.fetch(:drop_messages_on_flush_error, false),
        :drop_messages_on_full_buffer => options.fetch(:drop_messages_on_full_buffer, false),
        :flush_at_exit => options.fetch(:flush_at_exit, false)
      }

      if @buffer_config[:flush_at_exit]
        at_exit { buffer_flush(final: true) }
      end

      reset_buffer
    end