function makeTouchable(TouchableComponent) {
    var Touchable = TouchableComponent || reactNative.Platform.select({
      android: reactNative.TouchableNativeFeedback,
      ios: reactNative.TouchableHighlight,
      default: reactNative.TouchableHighlight
    });
    var defaultTouchableProps = {};

    if (Touchable === reactNative.TouchableHighlight) {
      defaultTouchableProps = {
        underlayColor: 'rgba(0, 0, 0, 0.1)'
      };
    }

    return {
      Touchable: Touchable,
      defaultTouchableProps: defaultTouchableProps
    };
  }