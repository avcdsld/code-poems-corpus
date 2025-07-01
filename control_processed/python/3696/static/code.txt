def export_schema(cls, recursive=True, include_parent_ref=False):
        """Export schema as a dictionary"""
        parent_excludes = {}
        if not include_parent_ref:
            parent_ref = cls.__mapper__.relationships.get(cls.export_parent)
            if parent_ref:
                parent_excludes = {c.name for c in parent_ref.local_columns}

        def formatter(c):
            return ('{0} Default ({1})'.format(
                str(c.type), c.default.arg) if c.default else str(c.type))

        schema = {c.name: formatter(c) for c in cls.__table__.columns
                  if (c.name in cls.export_fields and
                  c.name not in parent_excludes)}
        if recursive:
            for c in cls.export_children:
                child_class = cls.__mapper__.relationships[c].argument.class_
                schema[c] = [child_class.export_schema(recursive=recursive,
                             include_parent_ref=include_parent_ref)]
        return schema