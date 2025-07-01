public static ScoringInfo[] prependScoringInfo(ScoringInfo scoringInfo, ScoringInfo[] scoringInfos) {
    if (scoringInfos == null) {
      return new ScoringInfo[]{ scoringInfo };
    } else {
      ScoringInfo[] bigger = new ScoringInfo[scoringInfos.length + 1];
      System.arraycopy(scoringInfos, 0, bigger, 0, scoringInfos.length);
      bigger[bigger.length - 1] = scoringInfo;
      return bigger;
    }
  }