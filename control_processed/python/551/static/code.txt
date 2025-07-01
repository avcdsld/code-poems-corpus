def _ensure_initialized(cls, instance=None, gateway=None, conf=None):
        """
        Checks whether a SparkContext is initialized or not.
        Throws error if a SparkContext is already running.
        """
        with SparkContext._lock:
            if not SparkContext._gateway:
                SparkContext._gateway = gateway or launch_gateway(conf)
                SparkContext._jvm = SparkContext._gateway.jvm

            if instance:
                if (SparkContext._active_spark_context and
                        SparkContext._active_spark_context != instance):
                    currentMaster = SparkContext._active_spark_context.master
                    currentAppName = SparkContext._active_spark_context.appName
                    callsite = SparkContext._active_spark_context._callsite

                    # Raise error if there is already a running Spark context
                    raise ValueError(
                        "Cannot run multiple SparkContexts at once; "
                        "existing SparkContext(app=%s, master=%s)"
                        " created by %s at %s:%s "
                        % (currentAppName, currentMaster,
                            callsite.function, callsite.file, callsite.linenum))
                else:
                    SparkContext._active_spark_context = instance