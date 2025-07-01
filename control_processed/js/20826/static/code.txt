function isReachViolation(importPath) {
      const steps = normalizeSep(importPath)
        .split('/')
        .reduce((acc, step) => {
          if (!step || step === '.') {
            return acc
          } else if (step === '..') {
            return acc.slice(0, -1)
          } else {
            return acc.concat(step)
          }
        }, [])

      const nonScopeSteps = steps.filter(step => step.indexOf('@') !== 0)
      if (nonScopeSteps.length <= 1) return false

      // before trying to resolve, see if the raw import (with relative
      // segments resolved) matches an allowed pattern
      const justSteps = steps.join('/')
      if (reachingAllowed(justSteps) || reachingAllowed(`/${justSteps}`)) return false

      // if the import statement doesn't match directly, try to match the
      // resolved path if the import is resolvable
      const resolved = resolve(importPath, context)
      if (!resolved || reachingAllowed(normalizeSep(resolved))) return false

      // this import was not allowed by the allowed paths, and reaches
      // so it is a violation
      return true
    }