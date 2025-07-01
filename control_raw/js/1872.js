function drawResults(canvas, poses, minPartConfidence, minPoseConfidence) {
  renderImageToCanvas(image, [513, 513], canvas);
  poses.forEach((pose) => {
    if (pose.score >= minPoseConfidence) {
      if (guiState.showKeypoints) {
        drawKeypoints(
            pose.keypoints, minPartConfidence, canvas.getContext('2d'));
      }

      if (guiState.showSkeleton) {
        drawSkeleton(
            pose.keypoints, minPartConfidence, canvas.getContext('2d'));
      }

      if (guiState.showBoundingBox) {
        drawBoundingBox(pose.keypoints, canvas.getContext('2d'));
      }
    }
  });
}