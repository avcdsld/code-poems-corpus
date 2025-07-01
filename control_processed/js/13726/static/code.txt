function writePodFile(result) {
  if (!fs.existsSync(directories.ios)) {
    fs.mkdirSync(directories.ios);
  }
  try {
    fs.writeFileSync(directories.ios + '/Podfile',
// The MLVision pod requires a minimum of iOS 9, otherwise the build will fail
(isPresent(result.ml_kit) ? `` : `#`) + `platform :ios, '9.0'

# With NativeScript < 5.2 we can't bump Firebase/Core beyond 5.15.0, but with 5.2+ we can
pod 'Firebase/Core', '~> ` + (supportsIOSModernBuildSystem ? '5.20.1' : '5.15.0') + `'

# Authentication
` + (!isPresent(result.authentication) || isSelected(result.authentication) ? `` : `#`) + `pod 'Firebase/Auth'

# Realtime DB
` + (!isPresent(result.realtimedb) || isSelected(result.realtimedb) ? `` : `#`) + `pod 'Firebase/Database'

# Cloud Firestore (sticking to 0.14 for now because of build error - see https://github.com/firebase/firebase-ios-sdk/issues/2177)
` + (isSelected(result.firestore) && !supportsIOSModernBuildSystem ? `` : `#`) + `pod 'FirebaseFirestore', '~> 0.14.0'
# .. unless the modern build system is supported, then we can use the latest version (NativeScript 5.2+)
` + (isSelected(result.firestore) && supportsIOSModernBuildSystem ? `` : `#`) + `pod 'Firebase/Firestore'

# Remote Config
` + (isSelected(result.remote_config) ? `` : `#`) + `pod 'Firebase/RemoteConfig'

# Performance Monitoring
` + (isSelected(result.performance_monitoring) ? `` : `#`) + `pod 'Firebase/Performance'

# Crash Reporting
` + (isSelected(result.crash_reporting) && !isSelected(result.crashlytics) ? `` : `#`) + `pod 'Firebase/Crash'

# Crashlytics
` + (isSelected(result.crashlytics) ? `` : `#`) + `pod 'Fabric'
` + (isSelected(result.crashlytics) ? `` : `#`) + `pod 'Crashlytics'
` + (!isSelected(result.crashlytics) ? `` : `
# Crashlytics works best without bitcode
post_install do |installer|
    installer.pods_project.targets.each do |target|
        target.build_configurations.each do |config|
            config.build_settings['ENABLE_BITCODE'] = "NO"
            config.build_settings['CLANG_ALLOW_NON_MODULAR_INCLUDES_IN_FRAMEWORK_MODULES'] = "YES"
        end
    end
end`) + `

# Firebase Cloud Messaging (FCM)
` + (isSelected(result.messaging) && !isSelected(result.external_messaging) ? `` : `#`) + `pod 'Firebase/Messaging'

# Firebase In-App Messaging (supported on NativeScript 5.2+)
` + (isSelected(result.in_app_messaging) && supportsIOSModernBuildSystem ? `` : `#`) + `pod 'Firebase/InAppMessagingDisplay'

# Firebase Cloud Storage
` + (isSelected(result.storage) ? `` : `#`) + `pod 'Firebase/Storage'

# Firebase Cloud Functions
` + (isSelected(result.functions) ? `` : `#`) + `pod 'Firebase/Functions'

# AdMob
` + (isSelected(result.admob) ? `` : `#`) + `pod 'Firebase/AdMob'

# Invites
` + (isSelected(result.invites) ? `` : `#`) + `pod 'Firebase/Invites'

# Dynamic Links
` + (isSelected(result.dynamic_links) ? `` : `#`) + `pod 'Firebase/DynamicLinks'

# ML Kit
` + (isSelected(result.ml_kit) ? `` : `#`) + `pod 'Firebase/MLVision'
` + (isSelected(result.ml_kit) && isSelected(result.ml_kit_text_recognition) ? `` : `#`) + `pod 'Firebase/MLVisionTextModel'
` + (isSelected(result.ml_kit) && isSelected(result.ml_kit_barcode_scanning) ? `` : `#`) + `pod 'Firebase/MLVisionBarcodeModel'
` + (isSelected(result.ml_kit) && isSelected(result.ml_kit_face_detection) ? `` : `#`) + `pod 'Firebase/MLVisionFaceModel'
` + (isSelected(result.ml_kit) && isSelected(result.ml_kit_image_labeling) ? `` : `#`) + `pod 'Firebase/MLVisionLabelModel'
` + (isSelected(result.ml_kit) && isSelected(result.ml_kit_custom_model) ? `` : `#`) + `pod 'Firebase/MLModelInterpreter'
` + (isSelected(result.ml_kit) && isSelected(result.ml_kit_natural_language_identification) ? `` : `#`) + `pod 'Firebase/MLNaturalLanguage'
` + (isSelected(result.ml_kit) && isSelected(result.ml_kit_natural_language_identification) ? `` : `#`) + `pod 'Firebase/MLNLLanguageID'
` + (isSelected(result.ml_kit) && isSelected(result.ml_kit_natural_language_smartreply) ? `` : `#`) + `pod 'Firebase/MLCommon'
` + (isSelected(result.ml_kit) && isSelected(result.ml_kit_natural_language_smartreply) ? `` : `#`) + `pod 'Firebase/MLNLSmartReply'

# Facebook Authentication
` + (isSelected(result.facebook_auth) ? `` : `#`) + `pod 'FBSDKCoreKit', '~> 4.38.0'
` + (isSelected(result.facebook_auth) ? `` : `#`) + `pod 'FBSDKLoginKit', '~> 4.38.0'

# Google Authentication
` + (isSelected(result.google_auth) ? `` : `#`) + `pod 'GoogleSignIn'`);
    console.log('Successfully created iOS (Pod) file.');
  } catch (e) {
    console.log('Failed to create iOS (Pod) file.');
    console.log(e);
  }
}