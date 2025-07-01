def get_predicate_indices(tags: List[str]) -> List[int]:
    """
    Return the word indices of a predicate in BIO tags.
    """
    return [ind for ind, tag in enumerate(tags) if 'V' in tag]