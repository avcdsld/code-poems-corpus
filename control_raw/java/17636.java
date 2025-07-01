public static boolean isPlaceholderShape(int[] shape) {
        if(shape == null)
            return true;
        else {
            for(int i = 0; i < shape.length; i++) {
                if(shape[i] < 0)
                    return true;
            }
        }

        return false;
    }