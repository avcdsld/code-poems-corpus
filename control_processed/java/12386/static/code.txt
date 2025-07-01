@MainThread
  public void playAnimation() {
    if (compositionLayer == null) {
      lazyCompositionTasks.add(new LazyCompositionTask() {
        @Override
        public void run(LottieComposition composition) {
          playAnimation();
        }
      });
      return;
    }

    if (systemAnimationsEnabled || getRepeatCount() == 0) {
      animator.playAnimation();
    }
    if (!systemAnimationsEnabled) {
      setFrame((int) (getSpeed() < 0 ? getMinFrame() : getMaxFrame()));
    }
  }