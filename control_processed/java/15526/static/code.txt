private static MethodHandle defineClassJava9(MethodHandles.Lookup lookup) throws ReflectiveOperationException
  {

    // this is getting meta
    MethodHandle defineClass = lookup.unreflect(MethodHandles.Lookup.class.getMethod("defineClass", byte[].class));
    MethodHandle privateLookupIn = lookup.findStatic(
        MethodHandles.class,
        "privateLookupIn",
        MethodType.methodType(MethodHandles.Lookup.class, Class.class, MethodHandles.Lookup.class)
    );

    // bind privateLookupIn lookup argument to this method's lookup
    // privateLookupIn = (Class targetClass) -> privateLookupIn(MethodHandles.privateLookupIn(targetClass, lookup))
    privateLookupIn = MethodHandles.insertArguments(privateLookupIn, 1, lookup);

    // defineClass = (Class targetClass, byte[] byteCode) -> privateLookupIn(targetClass).defineClass(byteCode)
    defineClass = MethodHandles.filterArguments(defineClass, 0, privateLookupIn);

    // add a dummy String argument to match the corresponding JDK8 version
    // defineClass = (Class targetClass, byte[] byteCode, String className) -> defineClass(targetClass, byteCode)
    defineClass = MethodHandles.dropArguments(defineClass, 2, String.class);
    return defineClass;
  }