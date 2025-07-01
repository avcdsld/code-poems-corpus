public static Slice serialize(Geometry geometry)
    {
        requireNonNull(geometry, "input is null");
        DynamicSliceOutput output = new DynamicSliceOutput(100);
        writeGeometry(geometry, output);
        return output.slice();
    }