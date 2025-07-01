def method_missing(method, *args)
      if (label = workbook.defined_names[method.to_s])
        safe_send(sheet_for(label.sheet).cells[label.key], :value)
      else
        # call super for methods like #a1
        super
      end
    end