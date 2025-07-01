def remove_service(self, wait_timeout=10, sleep_wait=1):
        '''
        Removes the PAExec service and executable that was created as part of
        the create_service function. This does not remove any older executables
        or services from previous runs, use cleanup() instead for that purpose.
        '''

        # Stops/remove the PAExec service and removes the executable
        log.debug("Deleting PAExec service at the end of the process")
        wait_start = time.time()
        while True:
            try:
                self._client._service.delete()
            except SCMRException as exc:
                log.debug("Exception encountered while deleting service %s", repr(exc))
                if time.time() - wait_start > wait_timeout:
                    raise exc
                time.sleep(sleep_wait)
                continue
            break

        # delete the PAExec executable
        smb_tree = TreeConnect(
            self._client.session,
            r"\\{0}\ADMIN$".format(self._client.connection.server_name)
        )
        log.info("Connecting to SMB Tree %s", smb_tree.share_name)
        smb_tree.connect()

        wait_start = time.time()
        while True:
            try:
                log.info("Creating open to PAExec file with delete on close flags")
                self._client._delete_file(smb_tree, self._exe_file)
            except SMBResponseException as exc:
                log.debug("Exception deleting file %s %s", self._exe_file, repr(exc))
                if time.time() - wait_start > wait_timeout:
                    raise exc
                time.sleep(sleep_wait)
                continue
            break
        log.info("Disconnecting from SMB Tree %s", smb_tree.share_name)
        smb_tree.disconnect()