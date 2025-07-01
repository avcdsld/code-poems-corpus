def setup_option_actions(self, mute_inline_plotting, show_plot_outline):
        """Setup the actions to show in the cog menu."""
        self.setup_in_progress = True
        self.mute_inline_action = create_action(
            self, _("Mute inline plotting"),
            tip=_("Mute inline plotting in the ipython console."),
            toggled=lambda state:
            self.option_changed('mute_inline_plotting', state)
            )
        self.mute_inline_action.setChecked(mute_inline_plotting)

        self.show_plot_outline_action = create_action(
            self, _("Show plot outline"),
            tip=_("Show the plot outline."),
            toggled=self.show_fig_outline_in_viewer
            )
        self.show_plot_outline_action.setChecked(show_plot_outline)

        self.actions = [self.mute_inline_action, self.show_plot_outline_action]
        self.setup_in_progress = False