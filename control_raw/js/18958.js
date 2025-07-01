function swsCoreStats() {

    // Options
    this.options = null;

    // Timestamp when collecting statistics started
    this.startts = Date.now();

    // Statistics for all requests
    this.all = null;

    // Statistics for requests by method
    // Initialized with most frequent ones, other methods will be added on demand if actually used
    this.method = null;

    // System statistics
    this.sys = null;

    // CPU
    this.startTime  = null;
    this.startUsage = null;

    // Array with last 5 hrtime / cpuusage, to calculate CPU usage during the last second sliding window ( 5 ticks )
    this.startTimeAndUsage = null;

    // Prometheus metrics
    this.promClientMetrics = {};

    this.promClientMetrics.api_all_request_total = new promClient.Counter({
        name: swsUtil.swsMetrics.api_all_request_total.name,
        help: swsUtil.swsMetrics.api_all_request_total.help });

    this.promClientMetrics.api_all_success_total = new promClient.Counter({
        name: swsUtil.swsMetrics.api_all_success_total.name,
        help: swsUtil.swsMetrics.api_all_success_total.help });
    this.promClientMetrics.api_all_errors_total = new promClient.Counter({
        name: swsUtil.swsMetrics.api_all_errors_total.name,
        help: swsUtil.swsMetrics.api_all_errors_total.help });
    this.promClientMetrics.api_all_client_error_total = new promClient.Counter({
        name: swsUtil.swsMetrics.api_all_client_error_total.name,
        help: swsUtil.swsMetrics.api_all_client_error_total.help });
    this.promClientMetrics.api_all_server_error_total = new promClient.Counter({
        name: swsUtil.swsMetrics.api_all_server_error_total.name,
        help: swsUtil.swsMetrics.api_all_server_error_total.help });
    this.promClientMetrics.api_all_request_in_processing_total = new promClient.Gauge({
        name: swsUtil.swsMetrics.api_all_request_in_processing_total.name,
        help: swsUtil.swsMetrics.api_all_request_in_processing_total.help });

    this.promClientMetrics.nodejs_process_memory_rss_bytes = new promClient.Gauge({
        name: swsUtil.swsMetrics.nodejs_process_memory_rss_bytes.name,
        help: swsUtil.swsMetrics.nodejs_process_memory_rss_bytes.help });
    this.promClientMetrics.nodejs_process_memory_heap_total_bytes = new promClient.Gauge({
        name: swsUtil.swsMetrics.nodejs_process_memory_heap_total_bytes.name,
        help: swsUtil.swsMetrics.nodejs_process_memory_heap_total_bytes.help });
    this.promClientMetrics.nodejs_process_memory_heap_used_bytes = new promClient.Gauge({
        name: swsUtil.swsMetrics.nodejs_process_memory_heap_used_bytes.name,
        help: swsUtil.swsMetrics.nodejs_process_memory_heap_used_bytes.help });
    this.promClientMetrics.nodejs_process_memory_external_bytes = new promClient.Gauge({
        name: swsUtil.swsMetrics.nodejs_process_memory_external_bytes.name,
        help: swsUtil.swsMetrics.nodejs_process_memory_external_bytes.help });
    this.promClientMetrics.nodejs_process_cpu_usage_percentage = new promClient.Gauge({
        name: swsUtil.swsMetrics.nodejs_process_cpu_usage_percentage.name,
        help: swsUtil.swsMetrics.nodejs_process_cpu_usage_percentage.help });

}