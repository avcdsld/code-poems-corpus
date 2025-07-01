def write_outfile(method_name, file)
      schema = @load_schema.call(self)
      context = @load_context.call(self)
      result = schema.public_send(method_name, only: @only, except: @except, context: context)
      dir = File.dirname(file)
      FileUtils.mkdir_p(dir)
      File.write(file, result)
    end