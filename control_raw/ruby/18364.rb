def mock_proc(klass, methods, success, result, type)
      Proc.new do
        methods.each do |method|
          allow(klass).to receive(method) do |&block|
            outcome = Tzu::Outcome.new(success, result, type)
            outcome.handle(&block) if block
            outcome
          end
        end
      end
    end