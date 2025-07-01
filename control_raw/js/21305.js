function invokeToneAssistant(payload, maintainToneHistoryInContext) {
  tone_detection
    .invokeToneAsync(payload, toneAnalyzer)
    .then(tone => {
      tone_detection.updateUserTone(
        payload,
        tone,
        maintainToneHistoryInContext
      );
      assistant.message(payload, function(err, data) {
        if (err) {
          // APPLICATION-SPECIFIC CODE TO PROCESS THE ERROR
          // FROM ASSISTANT SERVICE
          console.error(JSON.stringify(err, null, 2));
        } else {
          // APPLICATION-SPECIFIC CODE TO PROCESS THE DATA
          // FROM ASSISTANT SERVICE
          console.log(JSON.stringify(data, null, 2));
        }
      });
    })
    .catch(function(err) {
      console.log(JSON.stringify(err, null, 2));
    });
}