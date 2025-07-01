public void setMinFrame(final int minFrame) {
    if (composition == null) {
      lazyCompositionTasks.add(new LazyCompositionTask() {
        @Override
        public void run(LottieComposition composition) {
          setMinFrame(minFrame);
        }
      });
      return;
    }
    animator.setMinFrame(minFrame);
  }