function removePassingAssertion(j, path) {
    // t.pass is a no op
    j(path)
        .find(j.CallExpression, {
            callee: {
                object: { name: 't' },
                property: { name: 'pass' },
            },
        })
        .remove();
}