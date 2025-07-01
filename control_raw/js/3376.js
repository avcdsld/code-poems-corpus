function (hookFn, origFn, before, after, repeatTest = 0) {
    const hookError = (hookName) => (e) => log.error(`Error in ${hookName}: ${e.stack}`)

    return origFn(function (...hookArgs) {
        // Print errors encountered in beforeHook and afterHook to console, but
        // don't propagate them to avoid failing the test. However, errors in
        // framework hook functions should fail the test, so propagate those.
        return executeHooksWithArgs(before).catch(hookError('beforeHook')).then(() => {
            /**
             * user wants handle async command using promises, no need to wrap in fiber context
             */
            if (hookFn.name === 'async') {
                return executeAsync.call(this, hookFn, repeatTest, filterSpecArgs(hookArgs))
            }

            return new Promise(runSync.call(this, hookFn, repeatTest, filterSpecArgs(hookArgs)))
        }).then(() => {
            return executeHooksWithArgs(after).catch(hookError('afterHook'))
        })
    })
}