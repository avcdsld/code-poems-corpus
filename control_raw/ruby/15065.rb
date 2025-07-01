def upload_from_archive(local_path, remote_path, properties = {})
      artifact = Resource::Artifact.new(local_path: local_path)
      artifact.upload_from_archive(key, remote_path, properties)
    end