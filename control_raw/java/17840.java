public SDVariable segmentMax(String name, SDVariable data, SDVariable segmentIds) {
        validateNumerical("segmentMax", "data", data);
        validateInteger("segmentMax", "segmentIds", segmentIds);
        SDVariable ret = f().segmentMax(data, segmentIds);
        return updateVariableNameAndReference(ret, name);
    }