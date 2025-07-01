def visit_FromImport(self, node, frame):
        """Visit named imports."""
        self.newline(node)
        self.write('included_template = %senvironment.get_template('
                   % (self.environment.is_async and 'await ' or ''))
        self.visit(node.template, frame)
        self.write(', %r).' % self.name)
        if node.with_context:
            self.write('make_module%s(context.get_all(), True, %s)'
                       % (self.environment.is_async and '_async' or '',
                          self.dump_local_context(frame)))
        elif self.environment.is_async:
            self.write('_get_default_module_async()')
        else:
            self.write('_get_default_module()')

        var_names = []
        discarded_names = []
        for name in node.names:
            if isinstance(name, tuple):
                name, alias = name
            else:
                alias = name
            self.writeline('%s = getattr(included_template, '
                           '%r, missing)' % (frame.symbols.ref(alias), name))
            self.writeline('if %s is missing:' % frame.symbols.ref(alias))
            self.indent()
            self.writeline('%s = undefined(%r %% '
                           'included_template.__name__, '
                           'name=%r)' %
                           (frame.symbols.ref(alias),
                            'the template %%r (imported on %s) does '
                            'not export the requested name %s' % (
                                self.position(node),
                                repr(name)
                           ), name))
            self.outdent()
            if frame.toplevel:
                var_names.append(alias)
                if not alias.startswith('_'):
                    discarded_names.append(alias)

        if var_names:
            if len(var_names) == 1:
                name = var_names[0]
                self.writeline('context.vars[%r] = %s' %
                               (name, frame.symbols.ref(name)))
            else:
                self.writeline('context.vars.update({%s})' % ', '.join(
                    '%r: %s' % (name, frame.symbols.ref(name)) for name in var_names
                ))
        if discarded_names:
            if len(discarded_names) == 1:
                self.writeline('context.exported_vars.discard(%r)' %
                               discarded_names[0])
            else:
                self.writeline('context.exported_vars.difference_'
                               'update((%s))' % ', '.join(imap(repr, discarded_names)))