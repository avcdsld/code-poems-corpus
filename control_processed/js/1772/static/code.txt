function rewriteFile(args, generator) {
    args.path = args.path || process.cwd();
    const fullPath = path.join(args.path, args.file);

    args.haystack = generator.fs.read(fullPath);
    const body = rewrite(args);
    generator.fs.write(fullPath, body);
}