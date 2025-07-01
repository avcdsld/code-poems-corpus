def __register(self, operator):
        """Registers the given logical operator to the environment and
        connects it to its upstream operator (if any).

        A call to this function adds a new edge to the logical topology.

        Attributes:
             operator (Operator): The metadata of the logical operator.
        """
        self.env.operators[operator.id] = operator
        self.dst_operator_id = operator.id
        logger.debug("Adding new dataflow edge ({},{}) --> ({},{})".format(
            self.src_operator_id,
            self.env.operators[self.src_operator_id].name,
            self.dst_operator_id,
            self.env.operators[self.dst_operator_id].name))
        # Update logical dataflow graphs
        self.env._add_edge(self.src_operator_id, self.dst_operator_id)
        # Keep track of the partitioning strategy and the destination operator
        src_operator = self.env.operators[self.src_operator_id]
        if self.is_partitioned is True:
            partitioning, _ = src_operator._get_partition_strategy(self.id)
            src_operator._set_partition_strategy(_generate_uuid(),
                                                 partitioning, operator.id)
        elif src_operator.type == OpType.KeyBy:
            # Set the output partitioning strategy to shuffle by key
            partitioning = PScheme(PStrategy.ShuffleByKey)
            src_operator._set_partition_strategy(_generate_uuid(),
                                                 partitioning, operator.id)
        else:  # No partitioning strategy has been defined - set default
            partitioning = PScheme(PStrategy.Forward)
            src_operator._set_partition_strategy(_generate_uuid(),
                                                 partitioning, operator.id)
        return self.__expand()