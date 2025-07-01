public String getAnnouncementPath(String listenerName)
  {
    return ZKPaths.makePath(
        getListenersPath(),
        Preconditions.checkNotNull(
            StringUtils.emptyToNullNonDruidDataString(listenerName), "Listener name cannot be null"
        )
    );
  }