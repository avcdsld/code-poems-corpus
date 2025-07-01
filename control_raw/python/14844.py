def _get_retry_delay(cause):
    """Helper for :func:`_delay_until_retry`.

    :type exc: :class:`grpc.Call`
    :param exc: exception for aborted transaction

    :rtype: float
    :returns: seconds to wait before retrying the transaction.
    """
    metadata = dict(cause.trailing_metadata())
    retry_info_pb = metadata.get("google.rpc.retryinfo-bin")
    if retry_info_pb is not None:
        retry_info = RetryInfo()
        retry_info.ParseFromString(retry_info_pb)
        nanos = retry_info.retry_delay.nanos
        return retry_info.retry_delay.seconds + nanos / 1.0e9