def _object_table(self, object_id):
        """Fetch and parse the object table information for a single object ID.

        Args:
            object_id: An object ID to get information about.

        Returns:
            A dictionary with information about the object ID in question.
        """
        # Allow the argument to be either an ObjectID or a hex string.
        if not isinstance(object_id, ray.ObjectID):
            object_id = ray.ObjectID(hex_to_binary(object_id))

        # Return information about a single object ID.
        message = self._execute_command(object_id, "RAY.TABLE_LOOKUP",
                                        ray.gcs_utils.TablePrefix.OBJECT, "",
                                        object_id.binary())
        if message is None:
            return {}
        gcs_entry = ray.gcs_utils.GcsTableEntry.GetRootAsGcsTableEntry(
            message, 0)

        assert gcs_entry.EntriesLength() > 0

        entry = ray.gcs_utils.ObjectTableData.GetRootAsObjectTableData(
            gcs_entry.Entries(0), 0)

        object_info = {
            "DataSize": entry.ObjectSize(),
            "Manager": entry.Manager(),
        }

        return object_info