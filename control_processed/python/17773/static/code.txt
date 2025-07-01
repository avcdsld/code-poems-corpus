def pull_image(self, image_name, stream=None):
        """
        Ask Docker to pull the container image with given name.

        Parameters
        ----------
        image_name str
            Name of the image
        stream samcli.lib.utils.stream_writer.StreamWriter
            Optional stream writer to output to. Defaults to stderr

        Raises
        ------
        DockerImagePullFailedException
            If the Docker image was not available in the server
        """
        stream_writer = stream or StreamWriter(sys.stderr)

        try:
            result_itr = self.docker_client.api.pull(image_name, stream=True, decode=True)
        except docker.errors.APIError as ex:
            LOG.debug("Failed to download image with name %s", image_name)
            raise DockerImagePullFailedException(str(ex))

        # io streams, especially StringIO, work only with unicode strings
        stream_writer.write(u"\nFetching {} Docker container image...".format(image_name))

        # Each line contains information on progress of the pull. Each line is a JSON string
        for _ in result_itr:
            # For every line, print a dot to show progress
            stream_writer.write(u'.')
            stream_writer.flush()

        # We are done. Go to the next line
        stream_writer.write(u"\n")