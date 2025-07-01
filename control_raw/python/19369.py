def _check_updates_ready(self):
        """Called by WorkerUpdates when ready"""
        from spyder.widgets.helperwidgets import MessageCheckBox

        # feedback` = False is used on startup, so only positive feedback is
        # given. `feedback` = True is used when after startup (when using the
        # menu action, and gives feeback if updates are, or are not found.
        feedback = self.give_updates_feedback

        # Get results from worker
        update_available = self.worker_updates.update_available
        latest_release = self.worker_updates.latest_release
        error_msg = self.worker_updates.error

        url_r = __project_url__ + '/releases'
        url_i = 'https://docs.spyder-ide.org/installation.html'

        # Define the custom QMessageBox
        box = MessageCheckBox(icon=QMessageBox.Information,
                              parent=self)
        box.setWindowTitle(_("Spyder updates"))
        box.set_checkbox_text(_("Check for updates on startup"))
        box.setStandardButtons(QMessageBox.Ok)
        box.setDefaultButton(QMessageBox.Ok)

        # Adjust the checkbox depending on the stored configuration
        section, option = 'main', 'check_updates_on_startup'
        check_updates = CONF.get(section, option)
        box.set_checked(check_updates)

        if error_msg is not None:
            msg = error_msg
            box.setText(msg)
            box.set_check_visible(False)
            box.exec_()
            check_updates = box.is_checked()
        else:
            if update_available:
                anaconda_msg = ''
                if 'Anaconda' in sys.version or 'conda-forge' in sys.version:
                    anaconda_msg = _("<hr><b>IMPORTANT NOTE:</b> It seems "
                                     "that you are using Spyder with "
                                     "<b>Anaconda/Miniconda</b>. Please "
                                     "<b>don't</b> use <code>pip</code> to "
                                     "update it as that will probably break "
                                     "your installation.<br><br>"
                                     "Instead, please wait until new conda "
                                     "packages are available and use "
                                     "<code>conda</code> to perform the "
                                     "update.<hr>")
                msg = _("<b>Spyder %s is available!</b> <br><br>Please use "
                        "your package manager to update Spyder or go to our "
                        "<a href=\"%s\">Releases</a> page to download this "
                        "new version. <br><br>If you are not sure how to "
                        "proceed to update Spyder please refer to our "
                        " <a href=\"%s\">Installation</a> instructions."
                        "") % (latest_release, url_r, url_i)
                msg += '<br>' + anaconda_msg
                box.setText(msg)
                box.set_check_visible(True)
                box.exec_()
                check_updates = box.is_checked()
            elif feedback:
                msg = _("Spyder is up to date.")
                box.setText(msg)
                box.set_check_visible(False)
                box.exec_()
                check_updates = box.is_checked()

        # Update checkbox based on user interaction
        CONF.set(section, option, check_updates)

        # Enable check_updates_action after the thread has finished
        self.check_updates_action.setDisabled(False)

        # Provide feeback when clicking menu if check on startup is on
        self.give_updates_feedback = True