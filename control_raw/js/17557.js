function loadTowers() {
  const internalTowersInfo = getInternalTowersInfo();
  const externalTowersInfo = getExternalTowersInfo();
  return uniqBy(internalTowersInfo.concat(externalTowersInfo), 'id').map(
    ({ id, requirePath }) => {
      const { name, description, levels } = require(requirePath); // eslint-disable-line global-require, import/no-dynamic-require
      return new Tower(id, name, description, levels);
    },
  );
}