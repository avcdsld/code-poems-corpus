function(fragment) {
            var keys = [];
            var tokenDiscoverer = Splunk.util._tokenDiscoverer;
            var keysToAdd;

            if (typeof fragment == 'string') {
                if (fragment.match(tokenDiscoverer)) {
                    keysToAdd = fragment.match(tokenDiscoverer);
                    // TODO - im sure there's a way to write the re so that it doesnt include the '$' chars but im moving on.
                    for (var i=0; i<keysToAdd.length; i++ ) {
                        keysToAdd[i] = keysToAdd[i].substring(1, keysToAdd[i].length-1);
                    }
                    return keysToAdd;
                }
                return [];
            }
            else if (typeof fragment == "function") {
                return [];
            }

            // then fragment is not a string.
            for (var key in fragment) {
                keysToAdd = [];
                keysToAdd = Splunk.util.discoverReplacementTokens(fragment[key]);

                // up until now we've only looked at values. We have to also discover keys in the key itself..
                var matchesInTheKeyItself = key.match(tokenDiscoverer) || [];
                for (var j=0; j<matchesInTheKeyItself.length; j++) {
                    // TODO - im sure there's a way to write the re so that it doesnt include the '$' chars but im moving on.
                    keysToAdd.push(matchesInTheKeyItself[j].substring(1, matchesInTheKeyItself[j].length-1));
                }
                // check against duplicates.
                for (var k=0; k<keysToAdd.length; k++) {
                    if (keys.indexOf(keysToAdd[k]) ==-1) {
                        keys.push(keysToAdd[k]);
                    }
                }
            }
            return keys;
        }