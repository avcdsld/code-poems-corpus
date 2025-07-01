def wrap_inference_results(inference_result_proto):
  """Returns packaged inference results from the provided proto.

  Args:
    inference_result_proto: The classification or regression response proto.

  Returns:
    An InferenceResult proto with the result from the response.
  """
  inference_proto = inference_pb2.InferenceResult()
  if isinstance(inference_result_proto,
                classification_pb2.ClassificationResponse):
    inference_proto.classification_result.CopyFrom(
        inference_result_proto.result)
  elif isinstance(inference_result_proto, regression_pb2.RegressionResponse):
    inference_proto.regression_result.CopyFrom(inference_result_proto.result)
  return inference_proto