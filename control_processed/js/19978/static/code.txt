function _findIndex(haystack, needle) {
            if (angular.isUndefined(haystack) || haystack.length === 0) {
                return -1;
            }

            for (var i = 0, len = haystack.length; i < len; i++) {
                if (haystack[i] === needle) {
                    return i;
                }
            }

            return -1;
        }