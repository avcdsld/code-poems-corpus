function isDateWithinRange(date, minDate, maxDate) {
       var dateAtMidnight = createDateAtMidnight(date);
       var minDateAtMidnight = isValidDate(minDate) ? createDateAtMidnight(minDate) : null;
       var maxDateAtMidnight = isValidDate(maxDate) ? createDateAtMidnight(maxDate) : null;
       return (!minDateAtMidnight || minDateAtMidnight <= dateAtMidnight) &&
           (!maxDateAtMidnight || maxDateAtMidnight >= dateAtMidnight);
     }