def random_string():
    """Generate a random string to use as an ID.

    Note that users may seed numpy, which could cause this function to generate
    duplicate IDs. Therefore, we need to seed numpy ourselves, but we can't
    interfere with the state of the user's random number generator, so we
    extract the state of the random number generator and reset it after we are
    done.

    TODO(rkn): If we want to later guarantee that these are generated in a
    deterministic manner, then we will need to make some changes here.

    Returns:
        A random byte string of length ray_constants.ID_SIZE.
    """
    # Get the state of the numpy random number generator.
    numpy_state = np.random.get_state()
    # Try to use true randomness.
    np.random.seed(None)
    # Generate the random ID.
    random_id = np.random.bytes(ray_constants.ID_SIZE)
    # Reset the state of the numpy random number generator.
    np.random.set_state(numpy_state)
    return random_id