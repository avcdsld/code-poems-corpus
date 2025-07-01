public static int[] validate4(int[] data, String paramName){
        if(data == null) {
            return null;
        }

        Preconditions.checkArgument(data.length == 1 || data.length == 2 || data.length == 4,
                "Need either 1, 2, or 4 %s values, got %s values: %s",
                paramName, data.length, data);

        if(data.length == 1){
            return new int[]{data[0], data[0], data[0], data[0]};
        } else if(data.length == 2){
            return new int[]{data[0], data[0], data[1], data[1]};
        } else {
            return data;
        }
    }