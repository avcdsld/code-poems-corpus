function setBlockUniforms(uniformBlockInfo, values) {
  const uniforms = uniformBlockInfo.uniforms;
  for (const name in values) {
    const array = uniforms[name];
    if (array) {
      const value = values[name];
      if (value.length) {
        array.set(value);
      } else {
        array[0] = value;
      }
    }
  }
}