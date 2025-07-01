function PostHTML (plugins) {
/**
 * PostHTML Instance
 *
 * @prop plugins
 * @prop options
 */
  this.version = pkg.version
  this.name = pkg.name
  this.plugins = typeof plugins === 'function' ? [plugins] : plugins || []

  /**
   * Tree messages to store and pass metadata between plugins
   *
   * @memberof tree
   * @type {Array} messages
   *
   * @example
   * ```js
   * export default function plugin (options = {}) {
   *   return function (tree) {
   *      tree.messages.push({
   *        type: 'dependency',
   *        file: 'path/to/dependency.html',
   *        from: tree.options.from
   *      })
   *
   *      return tree
   *   }
   * }
   * ```
   */
  this.messages = []

  // extend api methods
  Api.call(this)
}