void deleteWithChildren() {
    if (leaderboard != null) leaderboard.deleteWithChildren();

    if (gridKeys != null)
      for (Key<Grid> gridKey : gridKeys) gridKey.remove();

    // If the Frame was made here (e.g. buildspec contained a path, then it will be deleted
    if (buildSpec.input_spec.training_frame == null && origTrainingFrame != null) {
      origTrainingFrame.delete();
    }
    if (buildSpec.input_spec.validation_frame == null && validationFrame != null) {
      validationFrame.delete();
    }
    if (buildSpec.input_spec.leaderboard_frame == null && leaderboardFrame != null) {
      leaderboardFrame.delete();
    }
    delete();
  }