def closeEvent(self, event):
        """Reimplement Qt method."""
        self.plugin.dockwidget.setWidget(self.plugin)
        self.plugin.dockwidget.setVisible(True)
        self.plugin.switch_to_plugin()
        QMainWindow.closeEvent(self, event)
        self.plugin.undocked_window = None