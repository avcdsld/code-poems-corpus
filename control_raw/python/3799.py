def flower(port, address):
    """Runs a Celery Flower web server

    Celery Flower is a UI to monitor the Celery operation on a given
    broker"""
    BROKER_URL = celery_app.conf.BROKER_URL
    cmd = (
        'celery flower '
        f'--broker={BROKER_URL} '
        f'--port={port} '
        f'--address={address} '
    )
    logging.info(
        "The 'superset flower' command is deprecated. Please use the 'celery "
        "flower' command instead.")
    print(Fore.GREEN + 'Starting a Celery Flower instance')
    print(Fore.BLUE + '-=' * 40)
    print(Fore.YELLOW + cmd)
    print(Fore.BLUE + '-=' * 40)
    Popen(cmd, shell=True).wait()