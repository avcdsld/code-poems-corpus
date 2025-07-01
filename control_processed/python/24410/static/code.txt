def _get_model_without_dependencies(self, models_dict):
        '''
        Helper function to find the next model that should be created
        '''
        next_model = None
        if not models_dict:
            return next_model

        for model, dependencies in six.iteritems(models_dict):
            if dependencies == []:
                next_model = model
                break

        if next_model is None:
            raise ValueError('incomplete model definitions, models in dependency '
                             'list not defined: {0}'.format(models_dict))

        # remove the model from other depednencies before returning
        models_dict.pop(next_model)
        for model, dep_list in six.iteritems(models_dict):
            if next_model in dep_list:
                dep_list.remove(next_model)

        return next_model