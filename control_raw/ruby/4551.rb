def append(label, block)
      if store.key?(label.to_sym) && store[label.to_sym].respond_to?(:<<)
        store[label.to_sym] << block
      else
        store[label.to_sym] = []
        store[label.to_sym] << block
      end
    end