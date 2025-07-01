@SuppressWarnings("unchecked")
  public <T> boolean applyValueCallback(T property, @Nullable LottieValueCallback<T> callback) {
    if (property == TRANSFORM_ANCHOR_POINT) {
      if (anchorPoint == null) {
        anchorPoint = new ValueCallbackKeyframeAnimation(callback, new PointF());
      } else {
        anchorPoint.setValueCallback((LottieValueCallback<PointF>) callback);
      }
    } else if (property == TRANSFORM_POSITION) {
      if (position == null) {
        position = new ValueCallbackKeyframeAnimation(callback, new PointF());
      } else {
        position.setValueCallback((LottieValueCallback<PointF>) callback);
      }
    } else if (property == TRANSFORM_SCALE) {
      if (scale == null) {
        scale = new ValueCallbackKeyframeAnimation(callback, new ScaleXY());
      } else {
        scale.setValueCallback((LottieValueCallback<ScaleXY>) callback);
      }
    } else if (property == TRANSFORM_ROTATION) {
      if (rotation == null) {
        rotation = new ValueCallbackKeyframeAnimation(callback, 0f);
      } else {
        rotation.setValueCallback((LottieValueCallback<Float>) callback);
      }
    } else if (property == TRANSFORM_OPACITY) {
      if (opacity == null) {
        opacity = new ValueCallbackKeyframeAnimation(callback, 100);
      } else {
        opacity.setValueCallback((LottieValueCallback<Integer>) callback);
      }
    } else if (property == TRANSFORM_START_OPACITY && startOpacity != null) {
      if (startOpacity == null) {
        startOpacity = new ValueCallbackKeyframeAnimation(callback, 100);
      } else {
        startOpacity.setValueCallback((LottieValueCallback<Float>) callback);
      }
    } else if (property == TRANSFORM_END_OPACITY && endOpacity != null) {
      if (endOpacity == null) {
        endOpacity = new ValueCallbackKeyframeAnimation(callback, 100);
      } else {
        endOpacity.setValueCallback((LottieValueCallback<Float>) callback);
      }
    } else if (property == TRANSFORM_SKEW && skew != null) {
      if (skew == null) {
        skew = new FloatKeyframeAnimation(Collections.singletonList(new Keyframe<Float>(0f)));
      }
      skew.setValueCallback((LottieValueCallback<Float>) callback);
    } else if (property == TRANSFORM_SKEW_ANGLE && skewAngle != null) {
      if (skewAngle == null) {
        skewAngle = new FloatKeyframeAnimation(Collections.singletonList(new Keyframe<Float>(0f)));
      }
      skewAngle.setValueCallback((LottieValueCallback<Float>) callback);
    } else {
      return false;
    }
    return true;
  }