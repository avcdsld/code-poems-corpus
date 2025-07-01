def aggregate_metrics(latencies_ms, duration_ms, num_bucket):
    """Aggregates metrics."""
    overall_op_count = 0
    op_counts = {operation : len(latency) for operation,
                 latency in latencies_ms.iteritems()}
    overall_op_count = sum([op_count for op_count in op_counts.itervalues()])

    print('[OVERALL], RunTime(ms), %f' % duration_ms)
    print('[OVERALL], Throughput(ops/sec), %f' % (float(overall_op_count) /
                                                duration_ms * 1000.0))

    for operation in op_counts.keys():
        operation_upper = operation.upper()
        print('[%s], Operations, %d' % (operation_upper, op_counts[operation]))
        print('[%s], AverageLatency(us), %f' % (
            operation_upper, numpy.average(latencies_ms[operation]) * 1000.0))
        print('[%s], LatencyVariance(us), %f' % (
            operation_upper, numpy.var(latencies_ms[operation]) * 1000.0))
        print('[%s], MinLatency(us), %f' % (
            operation_upper, min(latencies_ms[operation]) * 1000.0))
        print('[%s], MaxLatency(us), %f' % (
            operation_upper, max(latencies_ms[operation]) * 1000.0))
        print('[%s], 95thPercentileLatency(us), %f' % (
            operation_upper,
            numpy.percentile(latencies_ms[operation], 95.0) * 1000.0))
        print('[%s], 99thPercentileLatency(us), %f' % (
            operation_upper,
            numpy.percentile(latencies_ms[operation], 99.0) * 1000.0))
        print('[%s], 99.9thPercentileLatency(us), %f' % (
            operation_upper,
            numpy.percentile(latencies_ms[operation], 99.9) * 1000.0))
        print('[%s], Return=OK, %d' % (operation_upper, op_counts[operation]))
        latency_array = numpy.array(latencies_ms[operation])
        for j in range(num_bucket):
            print('[%s], %d, %d' % (
                operation_upper, j,
                ((j <= latency_array) & (latency_array < (j + 1))).sum()))
        print('[%s], >%d, %d' % (operation_upper, num_bucket,
                                 (num_bucket <= latency_array).sum()))