public void multiplePutEntities(String keyName1, String keyName2) {
    Datastore datastore = transaction.getDatastore();
    // [START multiplePutEntities]
    Key key1 = datastore.newKeyFactory().setKind("MyKind").newKey(keyName1);
    Entity.Builder entityBuilder1 = Entity.newBuilder(key1);
    entityBuilder1.set("propertyName", "value1");
    Entity entity1 = entityBuilder1.build();

    Key key2 = datastore.newKeyFactory().setKind("MyKind").newKey(keyName2);
    Entity.Builder entityBuilder2 = Entity.newBuilder(key2);
    entityBuilder2.set("propertyName", "value2");
    Entity entity2 = entityBuilder2.build();

    transaction.put(entity1, entity2);
    transaction.commit();
    // [END multiplePutEntities]
  }