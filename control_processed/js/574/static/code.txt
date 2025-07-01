function completeBySourceData(data, sourceFormat, seriesLayoutBy, sourceHeader, dimensionsDefine) {
    if (!data) {
        return {dimensionsDefine: normalizeDimensionsDefine(dimensionsDefine)};
    }

    var dimensionsDetectCount;
    var startIndex;
    var findPotentialName;

    if (sourceFormat === SOURCE_FORMAT_ARRAY_ROWS) {
        // Rule: Most of the first line are string: it is header.
        // Caution: consider a line with 5 string and 1 number,
        // it still can not be sure it is a head, because the
        // 5 string may be 5 values of category columns.
        if (sourceHeader === 'auto' || sourceHeader == null) {
            arrayRowsTravelFirst(function (val) {
                // '-' is regarded as null/undefined.
                if (val != null && val !== '-') {
                    if (isString(val)) {
                        startIndex == null && (startIndex = 1);
                    }
                    else {
                        startIndex = 0;
                    }
                }
            // 10 is an experience number, avoid long loop.
            }, seriesLayoutBy, data, 10);
        }
        else {
            startIndex = sourceHeader ? 1 : 0;
        }

        if (!dimensionsDefine && startIndex === 1) {
            dimensionsDefine = [];
            arrayRowsTravelFirst(function (val, index) {
                dimensionsDefine[index] = val != null ? val : '';
            }, seriesLayoutBy, data);
        }

        dimensionsDetectCount = dimensionsDefine
            ? dimensionsDefine.length
            : seriesLayoutBy === SERIES_LAYOUT_BY_ROW
            ? data.length
            : data[0]
            ? data[0].length
            : null;
    }
    else if (sourceFormat === SOURCE_FORMAT_OBJECT_ROWS) {
        if (!dimensionsDefine) {
            dimensionsDefine = objectRowsCollectDimensions(data);
            findPotentialName = true;
        }
    }
    else if (sourceFormat === SOURCE_FORMAT_KEYED_COLUMNS) {
        if (!dimensionsDefine) {
            dimensionsDefine = [];
            findPotentialName = true;
            each(data, function (colArr, key) {
                dimensionsDefine.push(key);
            });
        }
    }
    else if (sourceFormat === SOURCE_FORMAT_ORIGINAL) {
        var value0 = getDataItemValue(data[0]);
        dimensionsDetectCount = isArray(value0) && value0.length || 1;
    }
    else if (sourceFormat === SOURCE_FORMAT_TYPED_ARRAY) {
        if (__DEV__) {
            assert(!!dimensionsDefine, 'dimensions must be given if data is TypedArray.');
        }
    }

    var potentialNameDimIndex;
    if (findPotentialName) {
        each(dimensionsDefine, function (dim, idx) {
            if ((isObject(dim) ? dim.name : dim) === 'name') {
                potentialNameDimIndex = idx;
            }
        });
    }

    return {
        startIndex: startIndex,
        dimensionsDefine: normalizeDimensionsDefine(dimensionsDefine),
        dimensionsDetectCount: dimensionsDetectCount,
        potentialNameDimIndex: potentialNameDimIndex
        // TODO: potentialIdDimIdx
    };
}