function isEquivalentType(typeA: GraphQLType, typeB: GraphQLType): boolean {
  // Easy short-circuit: equal types are equal.
  if (typeA === typeB) {
    return true;
  }

  // If either type is non-null, the other must also be non-null.
  if (typeA instanceof GraphQLNonNull && typeB instanceof GraphQLNonNull) {
    return isEquivalentType(typeA.ofType, typeB.ofType);
  }

  // If either type is a list, the other must also be a list.
  if (typeA instanceof GraphQLList && typeB instanceof GraphQLList) {
    return isEquivalentType(typeA.ofType, typeB.ofType);
  }

  // Make sure the two types are of the same class
  if (typeA.constructor.name === typeB.constructor.name) {
    const rawA = getRawType(typeA);
    const rawB = getRawType(typeB);

    // And they must have the exact same name
    return rawA.name === rawB.name;
  }

  // Otherwise the types are not equal.
  return false;
}