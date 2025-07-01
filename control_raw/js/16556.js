function registerClient(alias, urlToWsdl, clientStub) {
  aliasedClientStubs[alias] = clientStub;
  clientStubs[urlToWsdl] = clientStub;
}