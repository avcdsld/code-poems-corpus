function(id) {
                /*jshint -W040 */
                var customParams = paramsStore.get(id);
                customParams[filenameParam] = getName(id);

                return qq.s3.util.generateAwsParams({
                    endpoint: endpointStore.get(id),
                    clockDrift: clockDrift,
                    params: customParams,
                    type: handler._getMimeType(id),
                    bucket: upload.bucket.getName(id),
                    key: handler.getThirdPartyFileId(id),
                    accessKey: credentialsProvider.get().accessKey,
                    sessionToken: credentialsProvider.get().sessionToken,
                    acl: aclStore.get(id),
                    expectedStatus: expectedStatus,
                    minFileSize: validation.minSizeLimit,
                    maxFileSize: validation.maxSizeLimit,
                    reducedRedundancy: reducedRedundancy,
                    region: region,
                    serverSideEncryption: serverSideEncryption,
                    signatureVersion: signature.version,
                    log: log
                },
                qq.bind(requesters.policySignature.getSignature, this, id));
            }