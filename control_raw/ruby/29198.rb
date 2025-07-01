def instantiate_models_from_json(model_class, json)
      instantiate_models model_class, ResponseParser.parse(JSON.parse(json))
    end