def _sort_topk_votes(x, k):
    """
    Sort a dictionary of classes and corresponding vote totals according to the
    votes, then truncate to the highest 'k' classes.
    """
    y = sorted(x.items(), key=lambda x: x[1], reverse=True)[:k]
    return [{'class': i[0], 'votes': i[1]} for i in y]