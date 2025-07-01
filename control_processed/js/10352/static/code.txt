async function getFileSize(file) {
  const data = await readFileAsync(file, 'utf-8');
  return {
    fileSize: fileSize(Buffer.byteLength(data)),
    gzipSize: fileSize(await gzipSize(data))
  };
}