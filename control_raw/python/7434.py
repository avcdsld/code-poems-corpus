def load_docker_cache(tag, docker_registry) -> None:
    """Imports tagged container from the given docker registry"""
    if docker_registry:
        # noinspection PyBroadException
        try:
            import docker_cache
            logging.info('Docker cache download is enabled from registry %s', docker_registry)
            docker_cache.load_docker_cache(registry=docker_registry, docker_tag=tag)
        except Exception:
            logging.exception('Unable to retrieve Docker cache. Continue without...')
    else:
        logging.info('Distributed docker cache disabled')