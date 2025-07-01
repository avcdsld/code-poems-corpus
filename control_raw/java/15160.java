private ServerReflectionIndex updateIndexIfNecessary() {
    synchronized (lock) {
      if (serverReflectionIndex == null) {
        serverReflectionIndex =
            new ServerReflectionIndex(server.getImmutableServices(), server.getMutableServices());
        return serverReflectionIndex;
      }

      Set<FileDescriptor> serverFileDescriptors = new HashSet<>();
      Set<String> serverServiceNames = new HashSet<>();
      List<ServerServiceDefinition> serverMutableServices = server.getMutableServices();
      for (ServerServiceDefinition mutableService : serverMutableServices) {
        io.grpc.ServiceDescriptor serviceDescriptor = mutableService.getServiceDescriptor();
        if (serviceDescriptor.getSchemaDescriptor() instanceof ProtoFileDescriptorSupplier) {
          String serviceName = serviceDescriptor.getName();
          FileDescriptor fileDescriptor =
              ((ProtoFileDescriptorSupplier) serviceDescriptor.getSchemaDescriptor())
                  .getFileDescriptor();
          serverFileDescriptors.add(fileDescriptor);
          serverServiceNames.add(serviceName);
        }
      }

      // Replace the index if the underlying mutable services have changed. Check both the file
      // descriptors and the service names, because one file descriptor can define multiple
      // services.
      FileDescriptorIndex mutableServicesIndex = serverReflectionIndex.getMutableServicesIndex();
      if (!mutableServicesIndex.getServiceFileDescriptors().equals(serverFileDescriptors)
          || !mutableServicesIndex.getServiceNames().equals(serverServiceNames)) {
        serverReflectionIndex =
            new ServerReflectionIndex(server.getImmutableServices(), serverMutableServices);
      }

      return serverReflectionIndex;
    }
  }