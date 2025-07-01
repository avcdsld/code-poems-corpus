private Object readResolve() throws java.io.ObjectStreamException {
        return Nd4j.create(data, arrayShape, Nd4j.getStrides(arrayShape, arrayOrdering), 0, arrayOrdering);
    }