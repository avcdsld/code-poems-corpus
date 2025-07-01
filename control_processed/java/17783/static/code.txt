public SDVariable fill(String name, SDVariable shape, org.nd4j.linalg.api.buffer.DataType dataType, double value) {
        SDVariable result = f().fill(shape, dataType, value);
        return updateVariableNameAndReference(result, name);
    }