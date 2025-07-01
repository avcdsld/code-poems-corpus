def _check_cors_origin(origin, allowed_origins):
    '''
    Check if an origin match cors allowed origins
    '''
    if isinstance(allowed_origins, list):
        if origin in allowed_origins:
            return origin
    elif allowed_origins == '*':
        return allowed_origins
    elif allowed_origins == origin:
        # Cors origin is either * or specific origin
        return allowed_origins