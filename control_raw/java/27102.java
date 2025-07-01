public Map<String, String> orderQueryBuild() {
		Map<String, String> map = new HashMap<String, String>();
		if (getPayModel().equals(PayModel.SERVICEMODE)) {
			map.put("sub_mch_id", getSubMchId());
			map.put("sub_appid", getSubAppId());
		}

		map.put("appid", getAppId());
		map.put("mch_id", getMchId());

		if (StrKit.notBlank(getTransactionId())) {
			map.put("transaction_id", getTransactionId());
		} else {
			if (StrKit.isBlank(getOutTradeNo())) {
				throw new IllegalArgumentException("out_trade_no,transaction_id 不能同时为空");
			}
			map.put("out_trade_no", getOutTradeNo());
		}
		map.put("nonce_str", String.valueOf(System.currentTimeMillis()));
		map.put("sign", PaymentKit.createSign(map, getPaternerKey()));
		return map;
	}