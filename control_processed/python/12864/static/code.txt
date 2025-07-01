def tokenize(qp_pair, tokenizer=None, is_training=False):
    '''
    tokenize function.
    '''
    question_tokens = tokenizer.tokenize(qp_pair['question'])
    passage_tokens = tokenizer.tokenize(qp_pair['passage'])
    if is_training:
        question_tokens = question_tokens[:300]
        passage_tokens = passage_tokens[:300]
    passage_tokens.insert(
        0, {'word': '<BOS>', 'original_text': '<BOS>', 'char_begin': 0, 'char_end': 0})
    passage_tokens.append(
        {'word': '<EOS>', 'original_text': '<EOS>', 'char_begin': 0, 'char_end': 0})
    qp_pair['question_tokens'] = question_tokens
    qp_pair['passage_tokens'] = passage_tokens