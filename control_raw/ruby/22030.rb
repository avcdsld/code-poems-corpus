def load_from_file!(file)
      data = Psych.safe_load(File.read(file)) if File.file? file
      data = {} unless data.is_a? Hash
      conf = {}
      conf[:networks]     = Network.deserialize_all data['networks'], conf
      conf[:integrations] = Integration.deserialize_all data['integrations'],
                                                        conf
      conf
    end