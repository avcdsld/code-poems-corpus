def parse_deps(orig_doc, options={}):
    """Generate dependency parse in {'words': [], 'arcs': []} format.

    doc (Doc): Document do parse.
    RETURNS (dict): Generated dependency parse keyed by words and arcs.
    """
    doc = Doc(orig_doc.vocab).from_bytes(orig_doc.to_bytes())
    if not doc.is_parsed:
        user_warning(Warnings.W005)
    if options.get("collapse_phrases", False):
        with doc.retokenize() as retokenizer:
            for np in list(doc.noun_chunks):
                attrs = {
                    "tag": np.root.tag_,
                    "lemma": np.root.lemma_,
                    "ent_type": np.root.ent_type_,
                }
                retokenizer.merge(np, attrs=attrs)
    if options.get("collapse_punct", True):
        spans = []
        for word in doc[:-1]:
            if word.is_punct or not word.nbor(1).is_punct:
                continue
            start = word.i
            end = word.i + 1
            while end < len(doc) and doc[end].is_punct:
                end += 1
            span = doc[start:end]
            spans.append((span, word.tag_, word.lemma_, word.ent_type_))
        with doc.retokenize() as retokenizer:
            for span, tag, lemma, ent_type in spans:
                attrs = {"tag": tag, "lemma": lemma, "ent_type": ent_type}
                retokenizer.merge(span, attrs=attrs)
    if options.get("fine_grained"):
        words = [{"text": w.text, "tag": w.tag_} for w in doc]
    else:
        words = [{"text": w.text, "tag": w.pos_} for w in doc]
    arcs = []
    for word in doc:
        if word.i < word.head.i:
            arcs.append(
                {"start": word.i, "end": word.head.i, "label": word.dep_, "dir": "left"}
            )
        elif word.i > word.head.i:
            arcs.append(
                {
                    "start": word.head.i,
                    "end": word.i,
                    "label": word.dep_,
                    "dir": "right",
                }
            )
    return {"words": words, "arcs": arcs, "settings": get_doc_settings(orig_doc)}