function isOcspValidationDisabled(host)
{
  // ocsp is disabled if insecure-connect is enabled, or if we've disabled ocsp
  // for non-snowflake endpoints and the host is a non-snowflake endpoint
  return GlobalConfig.isInsecureConnect() || (Parameters.getValue(
          Parameters.names.JS_DRIVER_DISABLE_OCSP_FOR_NON_SF_ENDPOINTS) &&
      !REGEX_SNOWFLAKE_ENDPOINT.test(host));
}