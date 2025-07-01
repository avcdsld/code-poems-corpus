def fail(message = nil)
      if @__assert_pending__ == 0
        if halt_on_fail?
          raise Result::TestFailure, message || ""
        else
          capture_result(Assert::Result::Fail, message || "")
        end
      else
        if halt_on_fail?
          raise Result::TestSkipped, "Pending fail: #{message || ""}"
        else
          capture_result(Assert::Result::Skip, "Pending fail: #{message || ""}")
        end
      end
    end