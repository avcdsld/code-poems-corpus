public final void deleteProduct(String name) {

    DeleteProductRequest request = DeleteProductRequest.newBuilder().setName(name).build();
    deleteProduct(request);
  }