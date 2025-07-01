function(param) {
            var percentEncoded = encodeURIComponent(param);

            // %-encode characters not handled by `encodeURIComponent` (to follow RFC 3986)
            percentEncoded = percentEncoded.replace(/[!'()]/g, escape);

            // %-encode characters not handled by `escape` (to follow RFC 3986)
            percentEncoded = percentEncoded.replace(/\*/g, "%2A");

            // replace percent-encoded spaces with a "+"
            return percentEncoded.replace(/%20/g, "+");
        }