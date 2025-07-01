ValFrame addGlobals(Frame fr) {
    _ses.addGlobals(fr);
    return new ValFrame(new Frame(fr._names.clone(), fr.vecs().clone()));
  }