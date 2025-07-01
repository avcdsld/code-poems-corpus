function getMixinsFromFile(file, data) {

    /* Step 1: get all includes and insert them, so that at least empty mixins exist. */
    let regex = /@include ([a-z0-9-]+)/g;
    let match = regex.exec(data);

    while (match) {
        if (!(match[1] in themeMixins)) { themeMixins[match[1]] = `@mixin ${match[1]}(){}`; }
        if (!(match[1] in coreMixins)) { coreMixins[match[1]] = `@mixin ${match[1]}(){}`; }

        match = regex.exec(data);
    }

    /* Step 2: get all multiline mixins */
    regex = /@mixin ([\w-]*)\s*\((.*)\)\s*{\n(\s+[\w\W]+?)(?=\n})\n}/g;
    match = regex.exec(data);

    while (match) {
        themeMixins[match[1]] = match[0];
        if (file.indexOf('theme/') < 0) {
            coreMixins[match[1]] = match[0];
        }
        match = regex.exec(data);
    }

    /* Step 3: get all singleline mixins */
    regex = /@mixin ([\w-]*)\s*\((.*)\)\s*{( [^\n]+)}/g;
    match = regex.exec(data);

    while (match) {
        themeMixins[match[1]] = match[0];
        if (file.indexOf('theme/') < 0) {
            coreMixins[match[1]] = match[0];
        }

        match = regex.exec(data);
    }

    /* Step 4: remove the mixins from the file, so that users can overwrite them in their custom code. */
    return data
        .replace(/@mixin ([\w-]*)\s*\((.*)\)\s*{\n(\s+[\w\W]+?)(?=\n})\n}/g, '')
        .replace(/@mixin ([\w-]*)\s*\((.*)\)\s*{( [^\n]+)}/g, '');
}