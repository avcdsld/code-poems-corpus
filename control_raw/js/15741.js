function needleStyle(context, options, length, isRight) {
    return options.colorNeedleEnd ?
        drawings.linearGradient(context,
            isRight ? options.colorNeedleEnd : options.colorNeedle,
            isRight ? options.colorNeedle : options.colorNeedleEnd,
            length,
            !context.barDimensions.isVertical
        ) : options.colorNeedle;
}