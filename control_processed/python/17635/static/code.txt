def colorize_errors(event, colored):
        """
        Highlights some commonly known Lambda error cases in red:
            - Nodejs process crashes
            - Lambda function timeouts
        """

        nodejs_crash_msg = "Process exited before completing request"
        timeout_msg = "Task timed out"

        if nodejs_crash_msg in event.message \
                or timeout_msg in event.message:
            event.message = colored.red(event.message)

        return event