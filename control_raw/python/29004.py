def old_values(self):
        '''Returns the old values from the diff'''
        def get_old_values_and_key(item):
            values = item.old_values
            values.update({self._key: item.past_dict[self._key]})
            return values

        return [get_old_values_and_key(el)
                for el in self._get_recursive_difference('all')
                if el.diffs and el.past_dict]