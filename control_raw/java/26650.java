@SuppressWarnings("PMD.UnusedFormalParameter")
    @Override
    public Double getInstanceCPUSinceLastRun(String instanceId, long lastUpdated) {

//        long offsetInMilliseconds = Math.min(ONE_DAY_MILLI_SECOND,System.currentTimeMillis() - lastUpdated);
        Dimension instanceDimension = new Dimension().withName("InstanceId")
                .withValue(instanceId);

        Calendar cal = Calendar.getInstance();
        cal.add(Calendar.DAY_OF_YEAR, -1);
//        long oneDayAgo = cal.getTimeInMillis();

        GetMetricStatisticsRequest request = new GetMetricStatisticsRequest()
                .withMetricName("CPUUtilization")
                .withNamespace("AWS/EC2")
                .withPeriod(60 * 60)
                // one hour
                .withDimensions(instanceDimension)
                // to get metrics a specific
                // instance
                .withStatistics("Average")
                .withStartTime(new Date(new Date().getTime() - 1440 * 1000))
                .withEndTime(new Date());
        GetMetricStatisticsResult result = cloudWatchClient
                .getMetricStatistics(request);
        // to read data
        List<Datapoint> datapoints = result.getDatapoints();
        if (CollectionUtils.isEmpty(datapoints)) return 0.0;
        Datapoint datapoint = datapoints.get(0);
        return datapoint.getAverage();
    }