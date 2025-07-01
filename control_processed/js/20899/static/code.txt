function next_word_is_cap(sentence, i, parameter) {
  if (i < sentence.taggedWords.length - 1) {
    var next_word = sentence.taggedWords[i+1].token;
    return(next_word[0] === next_word[0].toUpperCase());
  }
  return(false);
}