def data(self):
        """This is the data object serialized to the js layer"""
        content = {
            'form_data': self.form_data,
            'token': self.token,
            'viz_name': self.viz_type,
            'filter_select_enabled': self.datasource.filter_select_enabled,
        }
        return content