def fetch_logs(self, lambda_name, filter_pattern='', limit=10000, start_time=0):
        """
        Fetch the CloudWatch logs for a given Lambda name.
        """
        log_name = '/aws/lambda/' + lambda_name
        streams = self.logs_client.describe_log_streams(
            logGroupName=log_name,
            descending=True,
            orderBy='LastEventTime'
        )

        all_streams = streams['logStreams']
        all_names = [stream['logStreamName'] for stream in all_streams]

        events = []
        response = {}
        while not response or 'nextToken' in response:
            extra_args = {}
            if 'nextToken' in response:
                extra_args['nextToken'] = response['nextToken']

            # Amazon uses millisecond epoch for some reason.
            # Thanks, Jeff.
            start_time = start_time * 1000
            end_time = int(time.time()) * 1000

            response = self.logs_client.filter_log_events(
                logGroupName=log_name,
                logStreamNames=all_names,
                startTime=start_time,
                endTime=end_time,
                filterPattern=filter_pattern,
                limit=limit,
                interleaved=True, # Does this actually improve performance?
                **extra_args
            )
            if response and 'events' in response:
                events += response['events']

        return sorted(events, key=lambda k: k['timestamp'])