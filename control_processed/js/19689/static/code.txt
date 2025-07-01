function dedupeDefaultVert() {
    const defaultVert = path.join(__dirname, 'tools/fragments/default.vert');
    const fragment = fs.readFileSync(defaultVert, 'utf8')
        .replace(/\n/g, '\\\\n')
        .replace(/([()*=.])/g, '\\$1');

    const pattern = new RegExp(`(var ([^=\\s]+)\\s?=\\s?)"${fragment}"`, 'g');

    return {
        name: 'dedupeDefaultVert',
        renderChunk(code) {
            const matches = [];
            let match;

            while ((match = pattern.exec(code)) !== null) {
                matches.push(match);
            }

            if (matches.length <= 1) {
                return null;
            }

            const str = new MagicString(code);
            const key = matches[0][2];

            for (let i = 1; i < matches.length; i++) {
                const match = matches[i];
                const start = code.indexOf(match[0]);

                str.overwrite(
                    start,
                    start + match[0].length,
                    match[1] + key
                );
            }

            return {
                code: str.toString(),
                map: str.generateMap({ hires: true }),
            };
        },
    };
}