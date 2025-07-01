function isAbstractType(type: GraphQLType): boolean {
  const rawType = getRawType(type);
  return (
    rawType instanceof GraphQLInterfaceType ||
    rawType instanceof GraphQLUnionType
  );
}