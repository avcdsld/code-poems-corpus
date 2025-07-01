def vbar_stack(self, stackers, **kw):
        ''' Generate multiple ``VBar`` renderers for levels stacked bottom
        to top.

        Args:
            stackers (seq[str]) : a list of data source field names to stack
                successively for ``left`` and ``right`` bar coordinates.

                Additionally, the ``name`` of the renderer will be set to
                the value of each successive stacker (this is useful with the
                special hover variable ``$name``)

        Any additional keyword arguments are passed to each call to ``vbar``.
        If a keyword value is a list or tuple, then each call will get one
        value from the sequence.

        Returns:
            list[GlyphRenderer]

        Examples:

            Assuming a ``ColumnDataSource`` named ``source`` with columns
            *2016* and *2017*, then the following call to ``vbar_stack`` will
            will create two ``VBar`` renderers that stack:

            .. code-block:: python

                p.vbar_stack(['2016', '2017'], x=10, width=0.9, color=['blue', 'red'], source=source)

            This is equivalent to the following two separate calls:

            .. code-block:: python

                p.vbar(bottom=stack(),       top=stack('2016'),         x=10, width=0.9, color='blue', source=source, name='2016')
                p.vbar(bottom=stack('2016'), top=stack('2016', '2017'), x=10, width=0.9, color='red',  source=source, name='2017')

        '''
        result = []
        for kw in _double_stack(stackers, "bottom", "top", **kw):
            result.append(self.vbar(**kw))
        return result