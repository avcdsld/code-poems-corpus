def is_connectable(port, host="localhost"):
    """
    Tries to connect to the server at port to see if it is running.

    :Args:
     - port - The port to connect.
    """
    socket_ = None
    try:
        socket_ = socket.create_connection((host, port), 1)
        result = True
    except _is_connectable_exceptions:
        result = False
    finally:
        if socket_:
            socket_.close()
    return result