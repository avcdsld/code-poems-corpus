def visit_Include(self, node, frame):
        """Handles includes."""
        if node.ignore_missing:
            self.writeline('try:')
            self.indent()

        func_name = 'get_or_select_template'
        if isinstance(node.template, nodes.Const):
            if isinstance(node.template.value, string_types):
                func_name = 'get_template'
            elif isinstance(node.template.value, (tuple, list)):
                func_name = 'select_template'
        elif isinstance(node.template, (nodes.Tuple, nodes.List)):
            func_name = 'select_template'

        self.writeline('template = environment.%s(' % func_name, node)
        self.visit(node.template, frame)
        self.write(', %r)' % self.name)
        if node.ignore_missing:
            self.outdent()
            self.writeline('except TemplateNotFound:')
            self.indent()
            self.writeline('pass')
            self.outdent()
            self.writeline('else:')
            self.indent()

        skip_event_yield = False
        if node.with_context:
            loop = self.environment.is_async and 'async for' or 'for'
            self.writeline('%s event in template.root_render_func('
                           'template.new_context(context.get_all(), True, '
                           '%s)):' % (loop, self.dump_local_context(frame)))
        elif self.environment.is_async:
            self.writeline('for event in (await '
                           'template._get_default_module_async())'
                           '._body_stream:')
        else:
            if supports_yield_from:
                self.writeline('yield from template._get_default_module()'
                               '._body_stream')
                skip_event_yield = True
            else:
                self.writeline('for event in template._get_default_module()'
                               '._body_stream:')

        if not skip_event_yield:
            self.indent()
            self.simple_write('event', frame)
            self.outdent()

        if node.ignore_missing:
            self.outdent()