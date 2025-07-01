def update(context=nil, options={})
      steps.each do |step|
        log_step(:before, step, context, options)
        begin
          step.last.call(context, options)
        rescue Exception => ex
          log_step(:error, step, context, options, ex)
          raise ex
        end
        log_step(:after, step, context, options)
      end
    end