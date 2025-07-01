function parseCustomValue(value, parse) {
  try {
    let parsed = parse(value)
    if (parsed === undefined) {
      return { value: null }
    }
    return { value: parsed }
  } catch (error) {
    return { error: error.message }
  }
}