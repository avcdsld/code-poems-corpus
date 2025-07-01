def configure_namespacebrowser(self):
        """Configure associated namespace browser widget"""
        # Update namespace view
        self.sig_namespace_view.connect(lambda data:
            self.namespacebrowser.process_remote_view(data))

        # Update properties of variables
        self.sig_var_properties.connect(lambda data:
            self.namespacebrowser.set_var_properties(data))