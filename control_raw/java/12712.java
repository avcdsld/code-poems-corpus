@com.netflix.servo.annotations.Monitor(name = "numOfASGQueryFailures",
            description = "Number of queries made to AWS to retrieve ASG information and that failed",
            type = DataSourceType.COUNTER)
    public long getNumberofASGQueryFailures() {
        return asgCache.stats().loadExceptionCount();
    }