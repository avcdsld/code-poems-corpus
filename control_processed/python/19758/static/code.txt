def document_did_save_notification(self, params):
        """
        Handle the textDocument/didSave message received from an LSP server.
        """
        text = None
        if 'text' in params:
            text = params['text']
        params = {
            'textDocument': {
                'uri': path_as_uri(params['file'])
            }
        }
        if text is not None:
            params['text'] = text
        return params