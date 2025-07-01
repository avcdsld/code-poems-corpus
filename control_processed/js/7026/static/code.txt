function(app) {
  var paths = [];

  var role;
  // master server should not come here
  if(app.isFrontend()) {
    role = 'frontend';
  } else {
    role = 'backend';
  }

  var sysPath = pathUtil.getSysRemotePath(role), serverType = app.getServerType();
  if(fs.existsSync(sysPath)) {
    paths.push(pathUtil.remotePathRecord('sys', serverType, sysPath));
  }
  var userPath = pathUtil.getUserRemotePath(app.getBase(), serverType);
  if(fs.existsSync(userPath)) {
    paths.push(pathUtil.remotePathRecord('user', serverType, userPath));
  }

  return paths;
}