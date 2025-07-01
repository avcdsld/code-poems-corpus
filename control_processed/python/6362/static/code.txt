def get_date_from_utterance(tokenized_utterance: List[Token],
                            year: int = 1993) -> List[datetime]:
    """
    When the year is not explicitly mentioned in the utterance, the query assumes that
    it is 1993 so we do the same here. If there is no mention of the month or day then
    we do not return any dates from the utterance.
    """

    dates = []

    utterance = ' '.join([token.text for token in tokenized_utterance])
    year_result = re.findall(r'199[0-4]', utterance)
    if year_result:
        year = int(year_result[0])
    trigrams = ngrams([token.text for token in tokenized_utterance], 3)
    for month, tens, digit in trigrams:
        # This will match something like ``september twenty first``.
        day = ' '.join([tens, digit])
        if month in MONTH_NUMBERS and day in DAY_NUMBERS:
            try:
                dates.append(datetime(year, MONTH_NUMBERS[month], DAY_NUMBERS[day]))
            except ValueError:
                print('invalid month day')

    bigrams = ngrams([token.text for token in tokenized_utterance], 2)
    for month, day in bigrams:
        if month in MONTH_NUMBERS and day in DAY_NUMBERS:
            # This will match something like ``september first``.
            try:
                dates.append(datetime(year, MONTH_NUMBERS[month], DAY_NUMBERS[day]))
            except ValueError:
                print('invalid month day')

    fivegrams = ngrams([token.text for token in tokenized_utterance], 5)
    for tens, digit, _, year_match, month in fivegrams:
        # This will match something like ``twenty first of 1993 july``.
        day = ' '.join([tens, digit])
        if month in MONTH_NUMBERS and day in DAY_NUMBERS and year_match.isdigit():
            try:
                dates.append(datetime(int(year_match), MONTH_NUMBERS[month], DAY_NUMBERS[day]))
            except ValueError:
                print('invalid month day')
        if month in MONTH_NUMBERS and digit in DAY_NUMBERS and year_match.isdigit():
            try:
                dates.append(datetime(int(year_match), MONTH_NUMBERS[month], DAY_NUMBERS[digit]))
            except ValueError:
                print('invalid month day')
    return dates