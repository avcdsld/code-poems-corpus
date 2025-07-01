function generateAggregate (aggregateOp, defaultColumnName = undefined) {
  let funcName = `get${_.upperFirst(aggregateOp)}`

  /**
   * Do not re-add the method if exists
   */
  if (KnexQueryBuilder.prototype[funcName]) {
    return
  }

  KnexQueryBuilder.prototype[funcName] = async function (columnName = defaultColumnName) {
    if (!columnName) {
      throw new Error(`'${funcName}' requires a column name.`)
    }

    const wrapper = new this.constructor(this.client)
    const query = wrapper.from(this.as('__lucid'))

    /**
     * Copy events from the original query
     */
    query._events = this._events

    /**
     * Executing query chain
     */
    const results = await query[aggregateOp](`${columnName} as __lucid_aggregate`)

    return results[0].__lucid_aggregate
  }
}