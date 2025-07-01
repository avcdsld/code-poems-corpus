public static boolean sign(Map<String, String> data, String encoding) {
		
		if (isEmpty(encoding)) {
			encoding = "UTF-8";
		}
		String signMethod = data.get(param_signMethod);
		String version = data.get(SDKConstants.param_version);
		if (!VERSION_1_0_0.equals(version) && !VERSION_5_0_1.equals(version) && isEmpty(signMethod)) {
			LogUtil.writeErrorLog("signMethod must Not null");
			return false;
		}
		
		if (isEmpty(version)) {
			LogUtil.writeErrorLog("version must Not null");
			return false;
		}
		if (SIGNMETHOD_RSA.equals(signMethod)|| VERSION_1_0_0.equals(version) || VERSION_5_0_1.equals(version)) {
			if (VERSION_5_0_0.equals(version)|| VERSION_1_0_0.equals(version) || VERSION_5_0_1.equals(version)) {
				// 设置签名证书序列号
				data.put(SDKConstants.param_certId, CertUtil.getSignCertId());
				// 将Map信息转换成key1=value1&key2=value2的形式
				String stringData = coverMap2String(data);
				LogUtil.writeLog("待签名请求报文串:[" + stringData + "]");
				byte[] byteSign = null;
				String stringSign = null;
				try {
					// 通过SHA1进行摘要并转16进制
					byte[] signDigest = SecureUtil
							.sha1X16(stringData, encoding);
					byteSign = SecureUtil.base64Encode(SecureUtil.signBySoft(
							CertUtil.getSignCertPrivateKey(), signDigest));
					stringSign = new String(byteSign);
					// 设置签名域值
					data.put(SDKConstants.param_signature, stringSign);
					return true;
				} catch (Exception e) {
					LogUtil.writeErrorLog("Sign Error", e);
					return false;
				}
			} else if (VERSION_5_1_0.equals(version)) {
				// 设置签名证书序列号
				data.put(SDKConstants.param_certId, CertUtil.getSignCertId());
				// 将Map信息转换成key1=value1&key2=value2的形式
				String stringData = coverMap2String(data);
				LogUtil.writeLog("待签名请求报文串:[" + stringData + "]");
				byte[] byteSign = null;
				String stringSign = null;
				try {
					// 通过SHA256进行摘要并转16进制
					byte[] signDigest = SecureUtil
							.sha256X16(stringData, encoding);
					byteSign = SecureUtil.base64Encode(SecureUtil.signBySoft256(
							CertUtil.getSignCertPrivateKey(), signDigest));
					stringSign = new String(byteSign);
					// 设置签名域值
					data.put(SDKConstants.param_signature, stringSign);
					return true;
				} catch (Exception e) {
					LogUtil.writeErrorLog("Sign Error", e);
					return false;
				}
			}
		} else if (SIGNMETHOD_SHA256.equals(signMethod)) {
			return signBySecureKey(data, SDKConfig.getConfig()
					.getSecureKey(), encoding);
		} else if (SIGNMETHOD_SM3.equals(signMethod)) {
			return signBySecureKey(data, SDKConfig.getConfig()
					.getSecureKey(), encoding);
		}
		return false;
	}