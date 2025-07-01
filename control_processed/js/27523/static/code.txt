function rewriteEndCallback(j, path) {
    // calls to t.end()
    const containsCalls =
        j(path)
            .find(j.CallExpression, {
                callee: {
                    object: { name: 't' },
                    property: { name: 'end' },
                },
            })
            .filter(p => {
                // if t.end is in the scope of the test function we remove it
                const outerParent = p.parent.parent.parent.node;
                const inTestScope =
                    outerParent.params &&
                    outerParent.params[0] &&
                    outerParent.params[0].name === 't';
                if (inTestScope) {
                    p.prune();
                    return null;
                }

                // else it might be used for async testing. We rename it to
                // familiar Jasmine 'done()'
                p.node.callee = j.identifier('done');
                return true;
            })
            .size() > 0;

    // references to t.end
    const containsReference =
        j(path)
            .find(j.MemberExpression, {
                object: { name: 't' },
                property: { name: 'end' },
            })
            .replaceWith(j.identifier('done'))
            .size() > 0;

    return containsCalls || containsReference;
}