function relayViewerHandleTransform(context: CompilerContext): CompilerContext {
  const viewerType = context.serverSchema.getType(VIEWER_TYPE);
  if (
    viewerType == null ||
    !(viewerType instanceof GraphQLObjectType) ||
    viewerType.getFields()[ID] != null
  ) {
    return context;
  }
  return IRTransformer.transform(context, {
    LinkedField: visitLinkedField,
  });
}