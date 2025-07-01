def print_csv(self, items, fields):
        """ print a set of fields in a set of items using a csv.writer

            Parameters
            ==========
            items: a list of items to print
            fields: a list of fields to select from items
        """
        writer = csv.writer(sys.stdout)
        writer.writerow(fields)
        for i in items:
            i_fields = [self.string(getattr(i, f)) for f in fields]
            writer.writerow(i_fields)