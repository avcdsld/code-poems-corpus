function visitDirective(directive: Directive): ?Directive {
  if (
    this.getContext()
      .serverSchema.getDirectives()
      .some(schemaDirective => schemaDirective.name === directive.name)
  ) {
    return directive;
  }
  return null;
}