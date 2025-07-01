def data_store(option)
      require "chef_zero/data_store/default_facade"

      store = case option
              when :in_memory
                require "chef_zero/data_store/memory_store_v2"
                ChefZero::DataStore::MemoryStoreV2.new
              when :on_disk
                require "tmpdir"
                require "chef_zero/data_store/raw_file_store"
                tmpdir = Dir.mktmpdir
                ChefZero::DataStore::RawFileStore.new(Dir.mktmpdir)
              else
                raise ArgumentError, ":#{option} is not a valid server_runner_data_store option. Please use either :in_memory or :on_disk."
              end

      ChefZero::DataStore::DefaultFacade.new(store, "chef", true)
    end