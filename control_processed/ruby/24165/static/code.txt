def generate_output(inputs, output)
      inputs.each do |input|
        output.write process_filters(input)
      end
    end