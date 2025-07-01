def mutant_charts_for_feature(example_protos, feature_name, serving_bundles,
                              viz_params):
  """Returns JSON formatted for rendering all charts for a feature.

  Args:
    example_proto: The example protos to mutate.
    feature_name: The string feature name to mutate.
    serving_bundles: One `ServingBundle` object per model, that contains the
      information to make the serving request.
    viz_params: A `VizParams` object that contains the UI state of the request.

  Raises:
    InvalidUserInputError if `viz_params.feature_index_pattern` requests out of
    range indices for `feature_name` within `example_proto`.

  Returns:
    A JSON-able dict for rendering a single mutant chart.  parsed in
    `tf-inference-dashboard.html`.
    {
      'chartType': 'numeric', # oneof('numeric', 'categorical')
      'data': [A list of data] # parseable by vz-line-chart or vz-bar-chart
    }
  """

  def chart_for_index(index_to_mutate):
    mutant_features, mutant_examples = make_mutant_tuples(
        example_protos, original_feature, index_to_mutate, viz_params)

    charts = []
    for serving_bundle in serving_bundles:
      inference_result_proto = run_inference(mutant_examples, serving_bundle)
      charts.append(make_json_formatted_for_single_chart(
        mutant_features, inference_result_proto, index_to_mutate))
    return charts
  try:
    original_feature = parse_original_feature_from_example(
        example_protos[0], feature_name)
  except ValueError as e:
    return {
        'chartType': 'categorical',
        'data': []
    }

  indices_to_mutate = viz_params.feature_indices or range(
      original_feature.length)
  chart_type = ('categorical' if original_feature.feature_type == 'bytes_list'
                else 'numeric')

  try:
    return {
        'chartType': chart_type,
        'data': [
            chart_for_index(index_to_mutate)
            for index_to_mutate in indices_to_mutate
        ]
    }
  except IndexError as e:
    raise common_utils.InvalidUserInputError(e)