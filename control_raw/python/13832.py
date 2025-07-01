def _cancel_grpc(operations_stub, operation_name):
    """Cancel an operation using a gRPC client.

    Args:
        operations_stub (google.longrunning.operations_pb2.OperationsStub):
            The gRPC operations stub.
        operation_name (str): The name of the operation.
    """
    request_pb = operations_pb2.CancelOperationRequest(name=operation_name)
    operations_stub.CancelOperation(request_pb)