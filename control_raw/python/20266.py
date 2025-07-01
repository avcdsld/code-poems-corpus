def dropEvent(self, event):
        """Override Qt method"""
        mimeData = event.mimeData()
        index_from = int(mimeData.data("source-index"))
        index_to = self.tabAt(event.pos())
        if index_to == -1:
            index_to = self.count()
        if int(mimeData.data("tabbar-id")) != id(self):
            tabwidget_from = to_text_string(mimeData.data("tabwidget-id"))
            
            # We pass self object ID as a QString, because otherwise it would 
            # depend on the platform: long for 64bit, int for 32bit. Replacing 
            # by long all the time is not working on some 32bit platforms 
            # (see Issue 1094, Issue 1098)
            self.sig_move_tab[(str, int, int)].emit(tabwidget_from, index_from,
                                                    index_to)
            event.acceptProposedAction()
        elif index_from != index_to:
            self.sig_move_tab.emit(index_from, index_to)
            event.acceptProposedAction()
        QTabBar.dropEvent(self, event)