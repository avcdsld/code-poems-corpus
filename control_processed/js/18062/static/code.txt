function flattenNormals(vertices) {
  if (vertices.indices) {
    throw "can't flatten normals of indexed vertices. deindex them first";
  }

  const normals = vertices.normal;
  const numNormals = normals.length;
  for (let ii = 0; ii < numNormals; ii += 9) {
    // pull out the 3 normals for this triangle
    const nax = normals[ii + 0];
    const nay = normals[ii + 1];
    const naz = normals[ii + 2];

    const nbx = normals[ii + 3];
    const nby = normals[ii + 4];
    const nbz = normals[ii + 5];

    const ncx = normals[ii + 6];
    const ncy = normals[ii + 7];
    const ncz = normals[ii + 8];

    // add them
    let nx = nax + nbx + ncx;
    let ny = nay + nby + ncy;
    let nz = naz + nbz + ncz;

    // normalize them
    const length = Math.sqrt(nx * nx + ny * ny + nz * nz);

    nx /= length;
    ny /= length;
    nz /= length;

    // copy them back in
    normals[ii + 0] = nx;
    normals[ii + 1] = ny;
    normals[ii + 2] = nz;

    normals[ii + 3] = nx;
    normals[ii + 4] = ny;
    normals[ii + 5] = nz;

    normals[ii + 6] = nx;
    normals[ii + 7] = ny;
    normals[ii + 8] = nz;
  }

  return vertices;
}