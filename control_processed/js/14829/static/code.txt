async function md5(entree) {
  const digest = md51(util.Uint8Array_to_str(entree));
  return util.hex_to_Uint8Array(hex(digest));
}