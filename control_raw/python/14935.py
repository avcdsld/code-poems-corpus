def get_model(client, model_id):
    """Sample ID: go/samples-tracker/1510"""

    # [START bigquery_get_model]
    from google.cloud import bigquery

    # TODO(developer): Construct a BigQuery client object.
    # client = bigquery.Client()

    # TODO(developer): Set model_id to the ID of the model to fetch.
    # model_id = 'your-project.your_dataset.your_model'

    model = client.get_model(model_id)

    full_model_id = "{}.{}.{}".format(model.project, model.dataset_id, model.model_id)
    friendly_name = model.friendly_name
    print(
        "Got model '{}' with friendly_name '{}'.".format(full_model_id, friendly_name)
    )