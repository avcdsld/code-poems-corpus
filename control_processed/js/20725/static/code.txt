function MailjetClient (api_key, api_secret, options, perform_api_call) {  
  return this.authStrategy(api_key, api_secret, options, perform_api_call)
}