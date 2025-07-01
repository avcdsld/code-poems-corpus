@Override
  public AddressBookParsedResult parse(Result result) {
    String rawText = getMassagedText(result);
    if (!rawText.startsWith("BIZCARD:")) {
      return null;
    }
    String firstName = matchSingleDoCoMoPrefixedField("N:", rawText, true);
    String lastName = matchSingleDoCoMoPrefixedField("X:", rawText, true);
    String fullName = buildName(firstName, lastName);
    String title = matchSingleDoCoMoPrefixedField("T:", rawText, true);
    String org = matchSingleDoCoMoPrefixedField("C:", rawText, true);
    String[] addresses = matchDoCoMoPrefixedField("A:", rawText, true);
    String phoneNumber1 = matchSingleDoCoMoPrefixedField("B:", rawText, true);
    String phoneNumber2 = matchSingleDoCoMoPrefixedField("M:", rawText, true);
    String phoneNumber3 = matchSingleDoCoMoPrefixedField("F:", rawText, true);
    String email = matchSingleDoCoMoPrefixedField("E:", rawText, true);

    return new AddressBookParsedResult(maybeWrap(fullName),
                                       null,
                                       null,
                                       buildPhoneNumbers(phoneNumber1, phoneNumber2, phoneNumber3),
                                       null,
                                       maybeWrap(email),
                                       null,
                                       null,
                                       null,
                                       addresses,
                                       null,
                                       org,
                                       null,
                                       title,
                                       null,
                                       null);
  }