def _process_api_events(self, function, api_events, template, condition=None):
        """
        Actually process given API events. Iteratively adds the APIs to Swagger JSON in the respective Serverless::Api
        resource from the template

        :param SamResource function: SAM Function containing the API events to be processed
        :param dict api_events: API Events extracted from the function. These events will be processed
        :param SamTemplate template: SAM Template where Serverless::Api resources can be found
        :param str condition: optional; this is the condition that is on the function with the API event
        """

        for logicalId, event in api_events.items():

            event_properties = event.get("Properties", {})
            if not event_properties:
                continue

            self._add_implicit_api_id_if_necessary(event_properties)

            api_id = self._get_api_id(event_properties)
            try:
                path = event_properties["Path"]
                method = event_properties["Method"]
            except KeyError as e:
                raise InvalidEventException(logicalId, "Event is missing key {}.".format(e))

            if (not isinstance(path, six.string_types)):
                raise InvalidEventException(logicalId,
                                            "Api Event must have a String specified for 'Path'.")
            if (not isinstance(method, six.string_types)):
                raise InvalidEventException(logicalId,
                                            "Api Event must have a String specified for 'Method'.")

            api_dict = self.api_conditions.setdefault(api_id, {})
            method_conditions = api_dict.setdefault(path, {})
            method_conditions[method] = condition

            self._add_api_to_swagger(logicalId, event_properties, template)

            api_events[logicalId] = event

        # We could have made changes to the Events structure. Write it back to function
        function.properties["Events"].update(api_events)