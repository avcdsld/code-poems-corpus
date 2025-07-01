def refresh_metrics(self):
        """Refresh metrics based on the column metadata"""
        metrics = self.get_metrics()
        dbmetrics = (
            db.session.query(DruidMetric)
            .filter(DruidMetric.datasource_id == self.datasource_id)
            .filter(DruidMetric.metric_name.in_(metrics.keys()))
        )
        dbmetrics = {metric.metric_name: metric for metric in dbmetrics}
        for metric in metrics.values():
            dbmetric = dbmetrics.get(metric.metric_name)
            if dbmetric:
                for attr in ['json', 'metric_type']:
                    setattr(dbmetric, attr, getattr(metric, attr))
            else:
                with db.session.no_autoflush:
                    metric.datasource_id = self.datasource_id
                    db.session.add(metric)