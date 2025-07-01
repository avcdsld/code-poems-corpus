public void setMaxFrame(final int maxFrame) {
    if (composition == null) {
      lazyCompositionTasks.add(new LazyCompositionTask() {
        @Override
        public void run(LottieComposition composition) {
          setMaxFrame(maxFrame);
        }
      });
      return;
    }
    animator.setMaxFrame(maxFrame + 0.99f);
  }