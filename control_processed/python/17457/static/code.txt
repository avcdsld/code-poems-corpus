def catch_error(func):
    """Catch errors of rabbitmq then reconnect"""
    import amqp
    try:
        import pika.exceptions
        connect_exceptions = (
            pika.exceptions.ConnectionClosed,
            pika.exceptions.AMQPConnectionError,
        )
    except ImportError:
        connect_exceptions = ()

    connect_exceptions += (
        select.error,
        socket.error,
        amqp.ConnectionError
    )

    def wrap(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except connect_exceptions as e:
            logging.error('RabbitMQ error: %r, reconnect.', e)
            self.reconnect()
            return func(self, *args, **kwargs)
    return wrap