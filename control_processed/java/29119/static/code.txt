@SuppressWarnings("WeakerAccess")
  public ApiFuture<Policy> setIamPolicyAsync(String instanceId, Policy policy) {
    String name = NameUtil.formatInstanceName(projectId, instanceId);
    final IamPolicyMarshaller marshaller = new IamPolicyMarshaller();

    SetIamPolicyRequest request =
        SetIamPolicyRequest.newBuilder()
            .setResource(name)
            .setPolicy(marshaller.toPb(policy))
            .build();

    return ApiFutures.transform(
        stub.setIamPolicyCallable().futureCall(request),
        new ApiFunction<com.google.iam.v1.Policy, Policy>() {
          @Override
          public Policy apply(com.google.iam.v1.Policy proto) {
            return marshaller.fromPb(proto);
          }
        },
        MoreExecutors.directExecutor());
  }