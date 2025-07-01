def datetime_to_str(self,format="%Y-%m-%dT%H:%M:%S%ZP"):
        """
        Create a new SArray with all the values cast to str. The string format is
        specified by the 'format' parameter.

        Parameters
        ----------
        format : str
            The format to output the string. Default format is "%Y-%m-%dT%H:%M:%S%ZP".

        Returns
        -------
        out : SArray[str]
            The SArray converted to the type 'str'.

        Examples
        --------
        >>> dt = datetime.datetime(2011, 10, 20, 9, 30, 10, tzinfo=GMT(-5))
        >>> sa = turicreate.SArray([dt])
        >>> sa.datetime_to_str("%e %b %Y %T %ZP")
        dtype: str
        Rows: 1
        [20 Oct 2011 09:30:10 GMT-05:00]

        See Also
        ----------
        str_to_datetime

        References
        ----------
        [1] Boost date time from string conversion guide (http://www.boost.org/doc/libs/1_48_0/doc/html/date_time/date_time_io.html)

        """
        if(self.dtype != datetime.datetime):
            raise TypeError("datetime_to_str expects SArray of datetime as input SArray")

        with cython_context():
            return SArray(_proxy=self.__proxy__.datetime_to_str(format))