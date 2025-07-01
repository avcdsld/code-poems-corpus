public final ErrorGroup getGroup(String groupName) {

    GetGroupRequest request = GetGroupRequest.newBuilder().setGroupName(groupName).build();
    return getGroup(request);
  }