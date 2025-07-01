def get_vertices(self, ids=[], fields={}, format='sframe'):
        """
        get_vertices(self, ids=list(), fields={}, format='sframe')
        Return a collection of vertices and their attributes.

        Parameters
        ----------

        ids : list [int | float | str] or SArray
            List of vertex IDs to retrieve. Only vertices in this list will be
            returned. Also accepts a single vertex id.

        fields : dict | pandas.DataFrame
            Dictionary specifying equality constraint on field values. For
            example ``{'gender': 'M'}``, returns only vertices whose 'gender'
            field is 'M'. ``None`` can be used to designate a wild card. For
            example, {'relationship': None} will find all vertices with the
            field 'relationship' regardless of the value.

        format : {'sframe', 'list'}
            Output format. The SFrame output (default) contains a column
            ``__src_id`` with vertex IDs and a column for each vertex attribute.
            List output returns a list of Vertex objects.

        Returns
        -------
        out : SFrame or list [Vertex]
            An SFrame or list of Vertex objects.

        See Also
        --------
        vertices, get_edges

        Examples
        --------
        Return all vertices in the graph.

        >>> from turicreate import SGraph, Vertex
        >>> g = SGraph().add_vertices([Vertex(0, attr={'gender': 'M'}),
                                       Vertex(1, attr={'gender': 'F'}),
                                       Vertex(2, attr={'gender': 'F'})])
        >>> g.get_vertices()
        +------+--------+
        | __id | gender |
        +------+--------+
        |  0   |   M    |
        |  2   |   F    |
        |  1   |   F    |
        +------+--------+

        Return vertices 0 and 2.

        >>> g.get_vertices(ids=[0, 2])
        +------+--------+
        | __id | gender |
        +------+--------+
        |  0   |   M    |
        |  2   |   F    |
        +------+--------+

        Return vertices with the vertex attribute "gender" equal to "M".

        >>> g.get_vertices(fields={'gender': 'M'})
        +------+--------+
        | __id | gender |
        +------+--------+
        |  0   |   M    |
        +------+--------+
        """

        if not _is_non_string_iterable(ids):
            ids = [ids]

        if type(ids) not in (list, SArray):
            raise TypeError('ids must be list or SArray type')

        with cython_context():
            sf = SFrame(_proxy=self.__proxy__.get_vertices(ids, fields))

        if (format == 'sframe'):
            return sf
        elif (format == 'dataframe'):
            assert HAS_PANDAS, 'Cannot use dataframe because Pandas is not available or version is too low.'
            if sf.num_rows() == 0:
                return pd.DataFrame()
            else:
                df = sf.head(sf.num_rows()).to_dataframe()
                return df.set_index('__id')
        elif (format == 'list'):
            return _dataframe_to_vertex_list(sf.to_dataframe())
        else:
            raise ValueError("Invalid format specifier")