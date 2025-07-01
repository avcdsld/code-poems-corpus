function parseError(error: Error | string | string[]): StackFrame[] {
  if (error == null) {
    throw new Error('You cannot pass a null object.')
  }
  if (typeof error === 'string') {
    return parseStack(error.split('\n'))
  }
  if (Array.isArray(error)) {
    return parseStack(error)
  }
  if (typeof error.stack === 'string') {
    return parseStack(error.stack.split('\n'))
  }
  throw new Error('The error you provided does not contain a stack trace.')
}