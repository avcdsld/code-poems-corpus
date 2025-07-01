@Override
   public void setHealthCheckRegistry(Object healthCheckRegistry)
   {
      boolean isAlreadySet = getHealthCheckRegistry() != null;
      super.setHealthCheckRegistry(healthCheckRegistry);

      HikariPool p = pool;
      if (p != null) {
         if (isAlreadySet) {
            throw new IllegalStateException("HealthCheckRegistry can only be set one time");
         }
         else {
            p.setHealthCheckRegistry(super.getHealthCheckRegistry());
         }
      }
   }