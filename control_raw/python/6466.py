def to_s3_uri(code_dict):
    """Constructs a S3 URI string from given code dictionary

    :param dict code_dict: Dictionary containing Lambda function Code S3 location of the form
                          {S3Bucket, S3Key, S3ObjectVersion}
    :return: S3 URI of form s3://bucket/key?versionId=version
    :rtype string
    """

    try:
        uri = "s3://{bucket}/{key}".format(bucket=code_dict["S3Bucket"], key=code_dict["S3Key"])
        version = code_dict.get("S3ObjectVersion", None)
    except (TypeError, AttributeError):
        raise TypeError("Code location should be a dictionary")

    if version:
        uri += "?versionId=" + version

    return uri