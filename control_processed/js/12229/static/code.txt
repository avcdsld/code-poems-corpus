function applyGdpr(bidderRequest, ortbRequest) {
  if (bidderRequest && bidderRequest.gdprConsent) {
    ortbRequest.regs = { ext: { gdpr: bidderRequest.gdprConsent.gdprApplies ? 1 : 0 } };
    ortbRequest.user = { ext: { consent: bidderRequest.gdprConsent.consentString } };
  }
}