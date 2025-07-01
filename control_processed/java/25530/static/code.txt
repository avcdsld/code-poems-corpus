public static String nameOfPersist(int x) {
    switch( x ) {
    case ICE : return "ICE";
    case HDFS: return "HDFS";
    case S3  : return "S3";
    case NFS : return "NFS";
    case TCP : return "TCP";
    case GCS : return "GCS";
    default  : return null;
    }
  }