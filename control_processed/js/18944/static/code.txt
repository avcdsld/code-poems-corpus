function getReference(model, embed, logger) {
  let property = model.schema.obj[embed]
  while (_.isArray(property)) {
    property = property[0]
  }
  if (property && property.ref) {
    return {
      model: property.ref,
      include: { model: globals.mongoose.model(property.ref), as: embed }
    }
  } else {
    return null
  }
}