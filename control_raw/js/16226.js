function inArray(elem, arr, i) {
        var len;

        if (arr) {
            if (Array$indexOf) {
                return Array$indexOf.call(arr, elem, i);
            }

            len = arr.length;
            i = i ? i < 0 ? Math.max(0, len + i) : i : 0;

            for (; i < len; i++) {
                // Skip accessing in sparse arrays
                if (i in arr && arr[i] === elem) {
                    return i;
                }
            }
        }

        return -1;
    }