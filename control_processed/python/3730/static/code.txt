def queries(self, last_updated_ms):
        """Get the updated queries."""
        stats_logger.incr('queries')
        if not g.user.get_id():
            return json_error_response(
                'Please login to access the queries.', status=403)

        # Unix time, milliseconds.
        last_updated_ms_int = int(float(last_updated_ms)) if last_updated_ms else 0

        # UTC date time, same that is stored in the DB.
        last_updated_dt = utils.EPOCH + timedelta(seconds=last_updated_ms_int / 1000)

        sql_queries = (
            db.session.query(Query)
            .filter(
                Query.user_id == g.user.get_id(),
                Query.changed_on >= last_updated_dt,
            )
            .all()
        )
        dict_queries = {q.client_id: q.to_dict() for q in sql_queries}

        now = int(round(time.time() * 1000))

        unfinished_states = [
            QueryStatus.PENDING,
            QueryStatus.RUNNING,
        ]

        queries_to_timeout = [
            client_id for client_id, query_dict in dict_queries.items()
            if (
                query_dict['state'] in unfinished_states and (
                    now - query_dict['startDttm'] >
                    config.get('SQLLAB_ASYNC_TIME_LIMIT_SEC') * 1000
                )
            )
        ]

        if queries_to_timeout:
            update(Query).where(
                and_(
                    Query.user_id == g.user.get_id(),
                    Query.client_id in queries_to_timeout,
                ),
            ).values(state=QueryStatus.TIMED_OUT)

            for client_id in queries_to_timeout:
                dict_queries[client_id]['status'] = QueryStatus.TIMED_OUT

        return json_success(
            json.dumps(dict_queries, default=utils.json_int_dttm_ser))