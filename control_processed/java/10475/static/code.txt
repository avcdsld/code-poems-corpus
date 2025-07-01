@Override
   public final void close() throws SQLException
   {
      synchronized (this) {
         if (isClosed) {
            return;
         }

         isClosed = true;
      }

      connection.untrackStatement(delegate);

      try {
         delegate.close();
      }
      catch (SQLException e) {
         throw connection.checkException(e);
      }
   }