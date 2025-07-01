function(num) {
            if(typeof num !== "number") {
                return NaN;
            }
            var isNegative = (num < 0),
                result;

            if(isNegative) {
                num = -num;
            }
            result = Math.pow(10, num);
            if(result < 10) {
                result = 10 * (result - 1) / (10 - 1);
            }
            result = (isNegative) ? -result : result;
            return (Math.round(result * 1000) / 1000);
        }