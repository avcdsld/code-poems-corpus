function runValidator(param, paramName) {
  if (!validator(param)) {
    console.log('Error message from validator: ' + validator.errors[0].message);
    console.log('Error message from validator: ', validator.errors[0]);
    throw new error.MalformedAstError(
      paramName +
        ' must be well-defined and follow the AST schema. ' +
        'Object: ' +
        JSON.stringify(param)
    );
  }
}