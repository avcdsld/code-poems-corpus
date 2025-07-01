def add_filter(self, property_name, operator, value):
        """Filter the query based on a property name, operator and a value.

        Expressions take the form of::

          .add_filter('<property>', '<operator>', <value>)

        where property is a property stored on the entity in the datastore
        and operator is one of ``OPERATORS``
        (ie, ``=``, ``<``, ``<=``, ``>``, ``>=``)::

          >>> from google.cloud import datastore
          >>> client = datastore.Client()
          >>> query = client.query(kind='Person')
          >>> query.add_filter('name', '=', 'James')
          >>> query.add_filter('age', '>', 50)

        :type property_name: str
        :param property_name: A property name.

        :type operator: str
        :param operator: One of ``=``, ``<``, ``<=``, ``>``, ``>=``.

        :type value: :class:`int`, :class:`str`, :class:`bool`,
                     :class:`float`, :class:`NoneType`,
                     :class:`datetime.datetime`,
                     :class:`google.cloud.datastore.key.Key`
        :param value: The value to filter on.

        :raises: :class:`ValueError` if ``operation`` is not one of the
                 specified values, or if a filter names ``'__key__'`` but
                 passes an invalid value (a key is required).
        """
        if self.OPERATORS.get(operator) is None:
            error_message = 'Invalid expression: "%s"' % (operator,)
            choices_message = "Please use one of: =, <, <=, >, >=."
            raise ValueError(error_message, choices_message)

        if property_name == "__key__" and not isinstance(value, Key):
            raise ValueError('Invalid key: "%s"' % value)

        self._filters.append((property_name, operator, value))