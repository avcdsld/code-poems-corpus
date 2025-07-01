def message(transformer = Undefined)
      return @custom_message if @custom_message

      transformer = self.transformer if Undefined.equal?(transformer)

      transformer.transform(self)
    end