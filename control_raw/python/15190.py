def list_blobs(self, prefix=''):
    """Lists names of all blobs by their prefix."""
    return [b.name for b in self.bucket.list_blobs(prefix=prefix)]