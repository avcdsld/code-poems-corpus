function shade(inputs, data) {
  const elevationImage = inputs[0];
  const width = elevationImage.width;
  const height = elevationImage.height;
  const elevationData = elevationImage.data;
  const shadeData = new Uint8ClampedArray(elevationData.length);
  const dp = data.resolution * 2;
  const maxX = width - 1;
  const maxY = height - 1;
  const pixel = [0, 0, 0, 0];
  const twoPi = 2 * Math.PI;
  const halfPi = Math.PI / 2;
  const sunEl = Math.PI * data.sunEl / 180;
  const sunAz = Math.PI * data.sunAz / 180;
  const cosSunEl = Math.cos(sunEl);
  const sinSunEl = Math.sin(sunEl);
  let pixelX, pixelY, x0, x1, y0, y1, offset,
      z0, z1, dzdx, dzdy, slope, aspect, cosIncidence, scaled;
  for (pixelY = 0; pixelY <= maxY; ++pixelY) {
    y0 = pixelY === 0 ? 0 : pixelY - 1;
    y1 = pixelY === maxY ? maxY : pixelY + 1;
    for (pixelX = 0; pixelX <= maxX; ++pixelX) {
      x0 = pixelX === 0 ? 0 : pixelX - 1;
      x1 = pixelX === maxX ? maxX : pixelX + 1;

      // determine elevation for (x0, pixelY)
      offset = (pixelY * width + x0) * 4;
      pixel[0] = elevationData[offset];
      pixel[1] = elevationData[offset + 1];
      pixel[2] = elevationData[offset + 2];
      pixel[3] = elevationData[offset + 3];
      z0 = data.vert * (pixel[0] + pixel[1] * 2 + pixel[2] * 3);

      // determine elevation for (x1, pixelY)
      offset = (pixelY * width + x1) * 4;
      pixel[0] = elevationData[offset];
      pixel[1] = elevationData[offset + 1];
      pixel[2] = elevationData[offset + 2];
      pixel[3] = elevationData[offset + 3];
      z1 = data.vert * (pixel[0] + pixel[1] * 2 + pixel[2] * 3);

      dzdx = (z1 - z0) / dp;

      // determine elevation for (pixelX, y0)
      offset = (y0 * width + pixelX) * 4;
      pixel[0] = elevationData[offset];
      pixel[1] = elevationData[offset + 1];
      pixel[2] = elevationData[offset + 2];
      pixel[3] = elevationData[offset + 3];
      z0 = data.vert * (pixel[0] + pixel[1] * 2 + pixel[2] * 3);

      // determine elevation for (pixelX, y1)
      offset = (y1 * width + pixelX) * 4;
      pixel[0] = elevationData[offset];
      pixel[1] = elevationData[offset + 1];
      pixel[2] = elevationData[offset + 2];
      pixel[3] = elevationData[offset + 3];
      z1 = data.vert * (pixel[0] + pixel[1] * 2 + pixel[2] * 3);

      dzdy = (z1 - z0) / dp;

      slope = Math.atan(Math.sqrt(dzdx * dzdx + dzdy * dzdy));

      aspect = Math.atan2(dzdy, -dzdx);
      if (aspect < 0) {
        aspect = halfPi - aspect;
      } else if (aspect > halfPi) {
        aspect = twoPi - aspect + halfPi;
      } else {
        aspect = halfPi - aspect;
      }

      cosIncidence = sinSunEl * Math.cos(slope) +
          cosSunEl * Math.sin(slope) * Math.cos(sunAz - aspect);

      offset = (pixelY * width + pixelX) * 4;
      scaled = 255 * cosIncidence;
      shadeData[offset] = scaled;
      shadeData[offset + 1] = scaled;
      shadeData[offset + 2] = scaled;
      shadeData[offset + 3] = elevationData[offset + 3];
    }
  }

  return {data: shadeData, width: width, height: height};
}