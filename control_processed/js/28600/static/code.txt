function maxWireVersion(topologyOrServer) {
  if (topologyOrServer.ismaster) {
    return topologyOrServer.ismaster.maxWireVersion;
  }

  if (topologyOrServer.description) {
    return topologyOrServer.description.maxWireVersion;
  }

  return null;
}