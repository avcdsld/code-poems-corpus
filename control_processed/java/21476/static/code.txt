public StackTraceElement filterFirst(Throwable target, boolean isInline) {
        boolean shouldSkip = isInline;

        if (GET_STACK_TRACE_ELEMENT != null) {
            int i = 0;

            // The assumption here is that the CLEANER filter will not filter out every single
            // element. However, since we don't want to compute the full length of the stacktrace,
            // we don't know the upper boundary. Therefore, simply increment the counter and go as
            // far as we have to go, assuming that we get there. If, in the rare occassion, we
            // don't, we fall back to the old slow path.
            while (true) {
                try {
                    StackTraceElement stackTraceElement =
                        (StackTraceElement)
                            GET_STACK_TRACE_ELEMENT.invoke(JAVA_LANG_ACCESS, target, i);

                    if (CLEANER.isIn(stackTraceElement)) {
                        if (shouldSkip) {
                            shouldSkip = false;
                        } else {
                            return stackTraceElement;
                        }
                    }
                } catch (Exception e) {
                    // Fall back to slow path
                    break;
                }
                i++;
            }
        }

        // If we can't use the fast path of retrieving stackTraceElements, use the slow path by
        // iterating over the actual stacktrace
        for (StackTraceElement stackTraceElement : target.getStackTrace()) {
            if (CLEANER.isIn(stackTraceElement)) {
                if (shouldSkip) {
                    shouldSkip = false;
                } else {
                    return stackTraceElement;
                }
            }
        }
        return null;
    }