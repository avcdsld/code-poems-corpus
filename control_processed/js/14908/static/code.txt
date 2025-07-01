function() {

    if (!this._alreadyInitiallyExpandedCriteria) {
      this._wlQueryInfo.criteria = expandWhereShorthand(this._wlQueryInfo.criteria);
      this._alreadyInitiallyExpandedCriteria = true;
    }//>-

    this._wlQueryInfo.criteria.groupBy = arguments[0];

    return this;
  }