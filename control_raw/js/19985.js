function _searchPath(container, regexp, previousKey, limitToFields) {
            limitToFields = limitToFields || [];
            limitToFields = (angular.isArray(limitToFields)) ? limitToFields : [limitToFields];

            var results = [];

            angular.forEach(container, function forEachItemsInContainer(items, key) {
                if (limitToFields.length > 0 && limitToFields.indexOf(key) === -1) {
                    return;
                }

                var pathToMatching = (previousKey) ? previousKey + '.' + key : key;

                var previousKeyAdded = false;
                var isLeaf = lxSelect.isLeaf(items);

                if ((!isLeaf && angular.isString(key) && regexp.test(key)) || (angular.isString(items) && regexp.test(items))) {
                    if (!previousKeyAdded && previousKey) {
                        results.push(previousKey);
                    }

                    if (!isLeaf) {
                        results.push(pathToMatching);
                    }
                }

                if (angular.isArray(items) || angular.isObject(items)) {
                    var newPaths = _searchPath(items, regexp, pathToMatching, (isLeaf) ? lxSelect.filterFields : []);

                    if (angular.isDefined(newPaths) && newPaths.length > 0) {
                        if (previousKey) {
                            results.push(previousKey);
                            previousKeyAdded = true;
                        }

                        results = results.concat(newPaths);
                    }
                }
            });

            return results;
        }