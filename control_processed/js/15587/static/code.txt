function(dataUri) {

            // first, make sure there are no newlines in the data uri
            dataUri = dataUri.replace(/\s/g, '');
            dataUri = decodeURIComponent(dataUri);

            var firstCommaIndex = dataUri.indexOf(','); // split dataUri as `dataTypeString`,`data`

            var dataTypeString = dataUri.slice(0, firstCommaIndex); // e.g. 'data:image/jpeg;base64'
            var mimeString = dataTypeString.split(':')[1].split(';')[0]; // e.g. 'image/jpeg'

            var data = dataUri.slice(firstCommaIndex + 1);
            var decodedString;
            if (dataTypeString.indexOf('base64') >= 0) { // data may be encoded in base64
                decodedString = atob(data); // decode data
            } else {
                // convert the decoded string to UTF-8
                decodedString = unescape(encodeURIComponent(data));
            }
            // write the bytes of the string to a typed array
            var ia = new Uint8Array(decodedString.length);
            for (var i = 0; i < decodedString.length; i++) {
                ia[i] = decodedString.charCodeAt(i);
            }

            return new Blob([ia], { type: mimeString }); // return the typed array as Blob
        }