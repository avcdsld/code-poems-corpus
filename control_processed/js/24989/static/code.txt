function inResult(event, operation) {
  switch (event.type) {
    case NORMAL:
      switch (operation) {
        case INTERSECTION:
          return !event.otherInOut;
        case UNION:
          return event.otherInOut;
        case DIFFERENCE:
          // return (event.isSubject && !event.otherInOut) ||
          //         (!event.isSubject && event.otherInOut);
          return (event.isSubject && event.otherInOut) ||
                  (!event.isSubject && !event.otherInOut);
        case XOR:
          return true;
      }
      break;
    case SAME_TRANSITION:
      return operation === INTERSECTION || operation === UNION;
    case DIFFERENT_TRANSITION:
      return operation === DIFFERENCE;
    case NON_CONTRIBUTING:
      return false;
  }
  return false;
}