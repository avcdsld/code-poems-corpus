function mergeExtraSegments(context, segments) {
    let currentSegments = segments;

    while (currentSegments.length > context.count) {
        const merged = [];

        for (let i = 0, length = currentSegments.length / 2 | 0; i < length; ++i) {
            merged.push(CodePathSegment.newNext(
                context.idGenerator.next(),
                [currentSegments[i], currentSegments[i + length]]
            ));
        }
        currentSegments = merged;
    }
    return currentSegments;
}