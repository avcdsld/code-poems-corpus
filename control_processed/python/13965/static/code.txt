def task_path(cls, project, location, queue, task):
        """Return a fully-qualified task string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/queues/{queue}/tasks/{task}",
            project=project,
            location=location,
            queue=queue,
            task=task,
        )