def _refresh_grpc(operations_stub, operation_name):
    """Refresh an operation using a gRPC client.

    Args:
        operations_stub (google.longrunning.operations_pb2.OperationsStub):
            The gRPC operations stub.
        operation_name (str): The name of the operation.

    Returns:
        google.longrunning.operations_pb2.Operation: The operation.
    """
    request_pb = operations_pb2.GetOperationRequest(name=operation_name)
    return operations_stub.GetOperation(request_pb)