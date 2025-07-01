function createUploadMetaResponseHandler({
  fileData,
  firebase,
  uploadTaskSnapshot,
  downloadURL
}) {
  /**
   * Converts upload meta data snapshot into an object (handling both
   * RTDB and Firestore)
   * @param  {Object} metaDataSnapshot - Snapshot from metadata upload (from
   * RTDB or Firestore)
   * @return {Object} Upload result including snapshot, key, File
   */
  return function uploadResultFromSnap(metaDataSnapshot) {
    const { useFirestoreForStorageMeta } = firebase._.config
    const result = {
      snapshot: metaDataSnapshot,
      key: metaDataSnapshot.key || metaDataSnapshot.id,
      File: fileData,
      metaDataSnapshot,
      uploadTaskSnapshot,
      // Support legacy method
      uploadTaskSnaphot: uploadTaskSnapshot,
      createdAt: useFirestoreForStorageMeta
        ? firebase.firestore.FieldValue.serverTimestamp()
        : firebase.database.ServerValue.TIMESTAMP
    }
    // Attach id if it exists (Firestore)
    if (metaDataSnapshot.id) {
      result.id = metaDataSnapshot.id
    }
    // Attach downloadURL if it exists
    if (downloadURL) {
      result.downloadURL = downloadURL
    }
    return result
  }
}