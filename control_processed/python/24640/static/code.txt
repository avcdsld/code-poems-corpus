def _create_doc(self):
        '''
        Create document.

        :return:
        '''
        root = etree.Element('image')
        root.set('schemaversion', '6.3')
        root.set('name', self.name)

        return root