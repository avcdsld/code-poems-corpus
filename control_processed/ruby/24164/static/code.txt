def generate_output(inputs, output)
      inputs.each do |input|
        output.write compile(input.read)
      end
    end