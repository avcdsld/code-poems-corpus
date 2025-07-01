function ExponentialRetryPolicyFilter(retryCount, retryInterval, minRetryInterval, maxRetryInterval) {
  this.retryCount = retryCount ? retryCount : ExponentialRetryPolicyFilter.DEFAULT_CLIENT_RETRY_COUNT;
  this.retryInterval = retryInterval ? retryInterval : ExponentialRetryPolicyFilter.DEFAULT_CLIENT_RETRY_INTERVAL;
  this.minRetryInterval = minRetryInterval ? minRetryInterval : ExponentialRetryPolicyFilter.DEFAULT_CLIENT_MIN_RETRY_INTERVAL;
  this.maxRetryInterval = maxRetryInterval ? maxRetryInterval : ExponentialRetryPolicyFilter.DEFAULT_CLIENT_MAX_RETRY_INTERVAL;
}