def format_cause(e)
      rv = curr = {}
      prev = nil

      cause_depth.times do
        break unless e.respond_to?(:cause) && e.cause

        cause = e.cause
        curr[:class]     = cause.class.name
        curr[:message]   = cause.message
        curr[:backtrace] = format_cause_backtrace(e, cause) if backtrace? && cause.backtrace

        prev[:cause] = curr unless prev.nil?
        prev, curr = curr, {}

        e = cause
      end

      if e.respond_to?(:cause) && e.cause
        prev[:cause] = {message: "Further #cause backtraces were omitted"}
      end

      rv
    end