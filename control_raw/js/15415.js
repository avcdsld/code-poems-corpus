function Tuple(n, args) {
    const parts = [].slice.call(args)
    if (n !== parts.length) {
      throw new TypeError(
        `${n}-Tuple: Expected ${n} values, but got ${parts.length}`
      )
    }

    const inspect = () =>
      `${n}-Tuple(${parts.map(_inspect).join(',')} )`

    function map(method) {
      return function(fn) {
        if (!isFunction(fn)) {
          throw new TypeError(`${n}-Tuple.${method}: Function required`)
        }

        return Tuple(n, parts
          .slice(0, parts.length - 1)
          .concat(fn(parts[parts.length - 1]))
        )
      }
    }

    const equals = m =>
      isSameType({ type }, m)
        && _equals(parts, m.toArray())

    function concat(method) {
      return function(t) {
        if (!isSameType({ type }, t)) {
          throw new TypeError(`${n}-Tuple.${method}: Tuple of the same length required`)
        }

        const a = t.toArray()

        return Tuple(n, parts.map((v, i, o) => {
          if (!(isSemigroup(a[i]) && isSemigroup(o[i]))) {
            throw new TypeError(
              `${n}-Tuple.${method}: Both Tuples must contain Semigroups of the same type`
            )
          }

          if (!isSameType(a[i], o[i])) {
            throw new TypeError(
              `${n}-Tuple.${method}: Both Tuples must contain Semigroups of the same type`
            )
          }

          return o[i].concat(a[i])
        }))
      }
    }

    function merge(fn) {
      if (!isFunction(fn)) {
        throw new TypeError(`${n}-Tuple.merge: Function required`)
      }

      return fn(...parts)
    }

    function mapAll(...args) {
      if (args.length !== parts.length) {
        throw new TypeError(
          `${n}-Tuple.mapAll: Requires ${parts.length} functions`
        )
      }

      return Tuple(
        n,
        parts.map((v, i) => {
          if (!isFunction(args[i])) {
            throw new TypeError(
              `${n}-Tuple.mapAll: Functions required for all arguments`
            )
          }
          return args[i](v)
        })
      )
    }

    function project(index) {
      if (!isInteger(index) || index < 1 || index > n) {
        throw new TypeError(
          `${n}-Tuple.project: Index should be an integer between 1 and ${n}`
        )
      }

      return parts[index - 1]
    }

    function toArray() {
      return parts.slice()
    }

    return {
      inspect, toString: inspect, merge,
      project, mapAll, toArray,
      tupleLength, type, equals,
      map: map('map'),
      concat: concat('concat'),
      [fl.map]: map(fl.map),
      [fl.concat]: concat(fl.concat),
      [fl.equals]: equals,
      ['@@type']: typeString,
      constructor: Tuple
    }
  }