def proxy_type(v):
    """ Match IP:PORT or DOMAIN:PORT in a losse manner """
    proxies = []
    if re.match(r"((http|socks5):\/\/.)?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})", v):
        proxies.append({"http": v,
                        "https": v})
        return proxies
    elif re.match(r"((http|socks5):\/\/.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}:(\d{1,5})", v):
        proxies.append({"http": v,
                        "https": v})
        return proxies
    elif is_proxy_list(v, proxies):
        return proxies
    else:
        raise argparse.ArgumentTypeError(
            "Proxy should follow IP:PORT or DOMAIN:PORT format")