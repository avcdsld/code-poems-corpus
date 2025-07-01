function(sortClause) {

    if (!this._alreadyInitiallyExpandedCriteria) {
      this._wlQueryInfo.criteria = expandWhereShorthand(this._wlQueryInfo.criteria);
      this._alreadyInitiallyExpandedCriteria = true;
    }//>-

    this._wlQueryInfo.criteria.sort = sortClause;

    return this;
  }