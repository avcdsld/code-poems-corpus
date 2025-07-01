def to_pb(self):
        """Render a protobuf message.

        Returns:
            google.iam.policy_pb2.Policy: a message to be passed to the
            ``set_iam_policy`` gRPC API.
        """

        return policy_pb2.Policy(
            etag=self.etag,
            version=self.version or 0,
            bindings=[
                policy_pb2.Binding(role=role, members=sorted(self[role]))
                for role in self
            ],
        )