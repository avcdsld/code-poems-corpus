public Map<String, String> pappayapplyBuild() {
		Map<String, String> map = new HashMap<String, String>();
		map.put("appid", getAppId());
		map.put("mch_id", getMchId());
		map.put("nonce_str", getNonceStr());
		map.put("body", getBody());
		map.put("attach", getAttach());
		map.put("out_trade_no", getOutTradeNo());
		map.put("total_fee", getTotalFee());
		map.put("spbill_create_ip", getSpbillCreateIp());
		map.put("notify_url", getNotifyUrl());
		map.put("trade_type", getTradeType().name());
		map.put("contract_id", getContractId());
		map.put("sign", PaymentKit.createSign(map, getPaternerKey()));
		return map;
	}