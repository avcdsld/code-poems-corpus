public static AlipayCommerceCityfacilitatorVoucherBatchqueryResponse voucherBatchqueryToResponse(
			AlipayCommerceCityfacilitatorVoucherBatchqueryModel model) throws AlipayApiException {
		AlipayCommerceCityfacilitatorVoucherBatchqueryRequest request = new AlipayCommerceCityfacilitatorVoucherBatchqueryRequest();
		request.setBizModel(model);
		return AliPayApiConfigKit.getAliPayApiConfig().getAlipayClient().execute(request);
	}