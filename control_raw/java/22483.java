private static long computeSizeof(Object obj, final IdentityHashMap visited,
                                      final Map /* <Class,ClassMetadata> */metadataMap) {
        // this uses depth-first traversal; the exact graph traversal algorithm
        // does not matter for computing the total size and this method could be
        // easily adjusted to do breadth-first instead (addLast() instead of
        // addFirst()),
        // however, dfs/bfs require max queue length to be the length of the
        // longest
        // graph path/width of traversal front correspondingly, so I expect
        // dfs to use fewer resources than bfs for most Java objects;

        if (null == obj || isSharedFlyweight(obj)) {
            return 0;
        }

        final LinkedList queue = new LinkedList();

        visited.put(obj, obj);
        queue.add(obj);

        long result = 0;

        final ClassAccessPrivilegedAction caAction = new ClassAccessPrivilegedAction();
        final FieldAccessPrivilegedAction faAction = new FieldAccessPrivilegedAction();

        while (!queue.isEmpty()) {
            obj = queue.removeFirst();
            final Class objClass = obj.getClass();

            int skippedBytes = skipClassDueToSunJVMBug(objClass);
            if (skippedBytes > 0) {
                result += skippedBytes; // can't do better than that
                continue;
            }

            if (objClass.isArray()) {
                final int arrayLength = Array.getLength(obj);
                final Class componentType = objClass.getComponentType();

                result += sizeofArrayShell(arrayLength, componentType);

                if (!componentType.isPrimitive()) {
                    // traverse each array slot:
                    for (int i = 0; i < arrayLength; ++i) {
                        final Object ref = Array.get(obj, i);

                        if ((ref != null) && !visited.containsKey(ref)) {
                            visited.put(ref, ref);
                            queue.addFirst(ref);
                        }
                    }
                }
            } else { // the object is of a non-array type
                final ClassMetadata metadata = getClassMetadata(objClass, metadataMap, caAction, faAction);
                final Field[] fields = metadata.m_refFields;

                result += metadata.m_shellSize;

                // traverse all non-null ref fields:
                for (int f = 0, fLimit = fields.length; f < fLimit; ++f) {
                    final Field field = fields[f];

                    final Object ref;
                    try { // to get the field value:
                        ref = field.get(obj);
                    } catch (Exception e) {
                        throw new RuntimeException("cannot get field [" + field.getName() + "] of class ["
                                                   + field.getDeclaringClass().getName() + "]: " + e.toString());
                    }

                    if ((ref != null) && !visited.containsKey(ref)) {
                        visited.put(ref, ref);
                        queue.addFirst(ref);
                    }
                }
            }
        }

        return result;
    }