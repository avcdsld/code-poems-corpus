public String encode(long... numbers) {
        if (numbers.length == 0) {
            return "";
        }

        for (final long number : numbers) {
            if (number < 0) {
                return "";
            }
            if (number > MAX_NUMBER) {
                throw new IllegalArgumentException("number can not be greater than " + MAX_NUMBER + "L");
            }
        }
        return this._encode(numbers);
    }