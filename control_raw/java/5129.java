static void configureArtifactServer(MesosArtifactServer server, ContainerSpecification container) throws IOException {
		// serve the artifacts associated with the container environment
		for (ContainerSpecification.Artifact artifact : container.getArtifacts()) {
			server.addPath(artifact.source, artifact.dest);
		}
	}