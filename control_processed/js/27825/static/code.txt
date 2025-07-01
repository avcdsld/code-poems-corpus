function updateProjectAccordingTo (platformConfig, locations) {
    // Update app name by editing res/values/strings.xml
    var strings = xmlHelpers.parseElementtreeSync(locations.strings);

    var name = platformConfig.name();
    strings.find('string[@name="app_name"]').text = name.replace(/\'/g, '\\\'');

    var shortName = platformConfig.shortName && platformConfig.shortName();
    if (shortName && shortName !== name) {
        strings.find('string[@name="launcher_name"]').text = shortName.replace(/\'/g, '\\\'');
    }

    fs.writeFileSync(locations.strings, strings.write({indent: 4}), 'utf-8');
    events.emit('verbose', 'Wrote out android application name "' + name + '" to ' + locations.strings);

    // Java packages cannot support dashes
    var androidPkgName = (platformConfig.android_packageName() || platformConfig.packageName()).replace(/-/g, '_');

    var manifest = new AndroidManifest(locations.manifest);
    var manifestId = manifest.getPackageId();

    manifest.getActivity()
        .setOrientation(platformConfig.getPreference('orientation'))
        .setLaunchMode(findAndroidLaunchModePreference(platformConfig));

    manifest.setVersionName(platformConfig.version())
        .setVersionCode(platformConfig.android_versionCode() || default_versionCode(platformConfig.version()))
        .setPackageId(androidPkgName)
        .setMinSdkVersion(platformConfig.getPreference('android-minSdkVersion', 'android'))
        .setMaxSdkVersion(platformConfig.getPreference('android-maxSdkVersion', 'android'))
        .setTargetSdkVersion(platformConfig.getPreference('android-targetSdkVersion', 'android'))
        .write();

    // Java file paths shouldn't be hard coded
    var javaPattern = path.join(locations.javaSrc, manifestId.replace(/\./g, '/'), '*.java');
    var java_files = shell.ls(javaPattern).filter(function (f) {
        return shell.grep(/extends\s+CordovaActivity/g, f);
    });

    if (java_files.length === 0) {
        throw new CordovaError('No Java files found that extend CordovaActivity.');
    } else if (java_files.length > 1) {
        events.emit('log', 'Multiple candidate Java files that extend CordovaActivity found. Guessing at the first one, ' + java_files[0]);
    }

    var destFile = path.join(locations.root, 'app', 'src', 'main', 'java', androidPkgName.replace(/\./g, '/'), path.basename(java_files[0]));
    shell.mkdir('-p', path.dirname(destFile));
    shell.sed(/package [\w\.]*;/, 'package ' + androidPkgName + ';', java_files[0]).to(destFile);
    events.emit('verbose', 'Wrote out Android package name "' + androidPkgName + '" to ' + destFile);

    var removeOrigPkg = checkReqs.isWindows() || checkReqs.isDarwin() ?
        manifestId.toUpperCase() !== androidPkgName.toUpperCase() :
        manifestId !== androidPkgName;

    if (removeOrigPkg) {
        // If package was name changed we need to remove old java with main activity
        shell.rm('-Rf', java_files[0]);
        // remove any empty directories
        var currentDir = path.dirname(java_files[0]);
        var sourcesRoot = path.resolve(locations.root, 'src');
        while (currentDir !== sourcesRoot) {
            if (fs.existsSync(currentDir) && fs.readdirSync(currentDir).length === 0) {
                fs.rmdirSync(currentDir);
                currentDir = path.resolve(currentDir, '..');
            } else {
                break;
            }
        }
    }
}