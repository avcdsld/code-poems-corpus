function highlightMatch(item, matchClass, rangeFilter) {
        var label = item.label || item;
        matchClass = matchClass || "quicksearch-namematch";

        var stringRanges = item.stringRanges;
        if (!stringRanges) {
            // If result didn't come from stringMatch(), highlight nothing
            stringRanges = [{
                text: label,
                matched: false,
                includesLastSegment: true
            }];
        }

        var displayName = "";
        if (item.scoreDebug) {
            var sd = item.scoreDebug;
            displayName += '<span title="sp:' + sd.special + ', m:' + sd.match +
                ', ls:' + sd.lastSegment + ', b:' + sd.beginning +
                ', ld:' + sd.lengthDeduction + ', c:' + sd.consecutive + ', nsos: ' +
                sd.notStartingOnSpecial + ', upper: ' + sd.upper + '">(' + item.matchGoodness + ') </span>';
        }

        // Put the path pieces together, highlighting the matched parts
        stringRanges.forEach(function (range) {
            if (range.matched) {
                displayName += "<span class='" + matchClass + "'>";
            }

            var rangeText = rangeFilter ? rangeFilter(range.includesLastSegment, range.text) : range.text;
            displayName += StringUtils.breakableUrl(rangeText);

            if (range.matched) {
                displayName += "</span>";
            }
        });
        return displayName;
    }