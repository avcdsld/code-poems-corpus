def register_pipeline(name, proc = nil, &block)
      proc ||= block

      self.config = hash_reassoc(config, :pipeline_exts) do |pipeline_exts|
        pipeline_exts.merge(".#{name}".freeze => name.to_sym)
      end

      self.config = hash_reassoc(config, :pipelines) do |pipelines|
        pipelines.merge(name.to_sym => proc)
      end
    end