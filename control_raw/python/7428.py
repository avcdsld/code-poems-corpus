def get_platforms(path: str = get_dockerfiles_path()) -> List[str]:
    """Get a list of architectures given our dockerfiles"""
    dockerfiles = glob.glob(os.path.join(path, "Dockerfile.*"))
    dockerfiles = list(filter(lambda x: x[-1] != '~', dockerfiles))
    files = list(map(lambda x: re.sub(r"Dockerfile.(.*)", r"\1", x), dockerfiles))
    platforms = list(map(lambda x: os.path.split(x)[1], sorted(files)))
    return platforms