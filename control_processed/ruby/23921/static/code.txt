def reserialize(new_serializer)
      if serializer == new_serializer
        return self
      end

      new_command = @command.deep_copy
      new_command.serializer = new_serializer

      PipelinedRDD.new(self, new_command)
    end