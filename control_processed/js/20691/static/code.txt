function validateStructure (apiDefinition) {
  var results = helpers.validateAgainstSchema(helpers.getJSONSchemaValidator(),
                                              swaggerSchema,
                                              apiDefinition.definitionFullyResolved);

  // Make complex JSON Schema validation errors easier to understand (Issue 15)
  results.errors = results.errors.map(function (error) {
    var defType = ['additionalProperties', 'items'].indexOf(error.path[error.path.length - 1]) > -1 ?
          'schema' :
          error.path[error.path.length - 2];

    if (['ANY_OF_MISSING', 'ONE_OF_MISSING'].indexOf(error.code) > -1) {
      switch (defType) {
      case 'parameters':
        defType = 'parameter';
        break;

      case 'responses':
        defType = 'response';
        break;

      case 'schema':
        defType += ' ' + error.path[error.path.length - 1];

        // no default
      }

      error.message = 'Not a valid ' + defType + ' definition';
    }

    return error;
  });

  // Treat invalid/missing references as structural errors
  _.each(apiDefinition.references, function (refDetails, refPtr) {
    var refPath = JsonRefs.pathFromPtr(refPtr);
    var err;

    if (refDetails.missing) {
      err = {
        code: 'UNRESOLVABLE_REFERENCE',
        message: 'Reference could not be resolved: ' + refDetails.uri,
        path: refPath.concat('$ref')
      };

      if (_.has(refDetails, 'error')) {
        err.error = refDetails.error;
      }

      results.errors.push(err);
    } else if (refDetails.type === 'invalid') {
      results.errors.push({
        code: 'INVALID_REFERENCE',
        message: refDetails.error || 'Invalid JSON Reference',
        path: refPath.concat('$ref')
      });
    } else if (_.has(refDetails, 'warning')) {
      // json-refs only creates warnings for JSON References with superfluous properties which will be ignored
      results.warnings.push({
        code: 'EXTRA_REFERENCE_PROPERTIES',
        message: refDetails.warning,
        path: refPath
      });
    }
  });

  return results;
}