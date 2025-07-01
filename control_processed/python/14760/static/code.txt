def to_api_repr(self):
        """Return a dictionary representing this schema field.

        Returns:
            dict: A dictionary representing the SchemaField in a serialized
                form.
        """
        # Put together the basic representation. See http://bit.ly/2hOAT5u.
        answer = {
            "mode": self.mode.upper(),
            "name": self.name,
            "type": self.field_type.upper(),
            "description": self.description,
        }

        # If this is a RECORD type, then sub-fields are also included,
        # add this to the serialized representation.
        if self.field_type.upper() == "RECORD":
            answer["fields"] = [f.to_api_repr() for f in self.fields]

        # Done; return the serialized dictionary.
        return answer