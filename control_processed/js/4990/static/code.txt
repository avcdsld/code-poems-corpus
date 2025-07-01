function create(
  fetchFn: FetchFunction,
  subscribeFn?: SubscribeFunction,
): Network {
  // Convert to functions that returns RelayObservable.
  const observeFetch = convertFetch(fetchFn);
  const observeSubscribe = subscribeFn
    ? convertSubscribe(subscribeFn)
    : undefined;

  function execute(
    request: RequestParameters,
    variables: Variables,
    cacheConfig: CacheConfig,
    uploadables?: ?UploadableMap,
  ): RelayObservable<GraphQLResponse> {
    if (request.operationKind === 'subscription') {
      invariant(
        observeSubscribe,
        'RelayNetwork: This network layer does not support Subscriptions. ' +
          'To use Subscriptions, provide a custom network layer.',
      );

      invariant(
        !uploadables,
        'RelayNetwork: Cannot provide uploadables while subscribing.',
      );
      return observeSubscribe(request, variables, cacheConfig);
    }

    const pollInterval = cacheConfig.poll;
    if (pollInterval != null) {
      invariant(
        !uploadables,
        'RelayNetwork: Cannot provide uploadables while polling.',
      );
      return observeFetch(request, variables, {force: true}).poll(pollInterval);
    }

    return observeFetch(request, variables, cacheConfig, uploadables);
  }

  return {execute};
}