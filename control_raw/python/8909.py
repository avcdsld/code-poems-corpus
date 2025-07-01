def get_help_option(self, ctx):
        """Returns the help option object."""
        help_options = self.get_help_option_names(ctx)
        if not help_options or not self.add_help_option:
            return

        def show_help(ctx, param, value):
            if value and not ctx.resilient_parsing:
                echo(ctx.get_help(), color=ctx.color)
                ctx.exit()
        return Option(help_options, is_flag=True,
                      is_eager=True, expose_value=False,
                      callback=show_help,
                      help='Show this message and exit.')