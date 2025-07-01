function extract_from_line (body) {
    const matches = body.bodytext.match(/\bFrom:[^<\n]*<([^>\n]*)>/);
    if (matches) {
        return matches[1];
    }

    for (let i=0,l=body.children.length; i < l; i++) {
        const from = extract_from_line(body.children[i]);
        if (from) {
            return from;
        }
    }

    return null;
}