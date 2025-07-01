def wice_grid_custom_filter_params(opts = {})
      options = {
        grid_name: 'grid',
        attribute: nil,
        model:     nil,
        value:     nil
      }
      options.merge!(opts)

      [:attribute, :value].each do |key|
        raise ::Wice::WiceGridArgumentError.new("wice_grid_custom_filter_params: :#{key} is a mandatory argument") unless options[key]
      end

      attr_name = if options[:model]
        unless options[:model].nil?
          options[:model] = options[:model].constantize if options[:model].is_a? String
          raise Wice::WiceGridArgumentError.new('Option :model can be either a class or a string instance') unless options[:model].is_a? Class
        end
        options[:model].table_name + '.' + options[:attribute]
      else
        options[:attribute]
      end

      { "#{options[:grid_name]}[f][#{attr_name}][]" => options[:value] }
    end