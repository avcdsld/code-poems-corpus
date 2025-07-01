def visit_Block(self, node, frame):
        """Call a block and register it for the template."""
        level = 0
        if frame.toplevel:
            # if we know that we are a child template, there is no need to
            # check if we are one
            if self.has_known_extends:
                return
            if self.extends_so_far > 0:
                self.writeline('if parent_template is None:')
                self.indent()
                level += 1

        if node.scoped:
            context = self.derive_context(frame)
        else:
            context = self.get_context_ref()

        if supports_yield_from and not self.environment.is_async and \
           frame.buffer is None:
            self.writeline('yield from context.blocks[%r][0](%s)' % (
                           node.name, context), node)
        else:
            loop = self.environment.is_async and 'async for' or 'for'
            self.writeline('%s event in context.blocks[%r][0](%s):' % (
                           loop, node.name, context), node)
            self.indent()
            self.simple_write('event', frame)
            self.outdent()

        self.outdent(level)