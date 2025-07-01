public final RecognizeResponse recognize(RecognitionConfig config, RecognitionAudio audio) {

    RecognizeRequest request =
        RecognizeRequest.newBuilder().setConfig(config).setAudio(audio).build();
    return recognize(request);
  }