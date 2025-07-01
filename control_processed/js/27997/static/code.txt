function extendData({
  data,
  lengthAngle: totalAngle,
  totalValue,
  paddingAngle,
}) {
  const total = totalValue || sumValues(data);
  const normalizedTotalAngle = valueBetween(totalAngle, -360, 360);
  const numberOfPaddings =
    Math.abs(normalizedTotalAngle) === 360 ? data.length : data.length - 1;
  const degreesTakenByPadding =
    Math.abs(paddingAngle) * numberOfPaddings * Math.sign(normalizedTotalAngle);
  const singlePaddingDegrees = degreesTakenByPadding / numberOfPaddings;
  const degreesTakenByPaths = normalizedTotalAngle - degreesTakenByPadding;
  let lastSegmentEnd = 0;

  return data.map(dataEntry => {
    const valueInPercentage = (dataEntry.value / total) * 100;
    const degrees = extractPercentage(degreesTakenByPaths, valueInPercentage);
    const startOffset = lastSegmentEnd;
    lastSegmentEnd = lastSegmentEnd + degrees + singlePaddingDegrees;

    return {
      percentage: valueInPercentage,
      degrees,
      startOffset,
      ...dataEntry,
    };
  });
}