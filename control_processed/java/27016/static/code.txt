public static AlipayCommerceCityfacilitatorVoucherRefundResponse metroRefundToResponse(
			AlipayCommerceCityfacilitatorVoucherRefundModel model) throws AlipayApiException {
		AlipayCommerceCityfacilitatorVoucherRefundRequest request = new AlipayCommerceCityfacilitatorVoucherRefundRequest();
		request.setBizModel(model);
		return AliPayApiConfigKit.getAliPayApiConfig().getAlipayClient().execute(request);
	}