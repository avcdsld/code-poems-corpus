private void writeObject(java.io.ObjectOutputStream s) throws IOException  {
    s.defaultWriteObject();     // Nothing to write
    for( Object K : keySet() ) {
      final Object V = get(K);  // Do an official 'get'
      s.writeObject(K);         // Write the <TypeK,TypeV> pair
      s.writeObject(V);
    }
    s.writeObject(null);        // Sentinel to indicate end-of-data
    s.writeObject(null);
  }