async function srcToDocs (dir) {
  const location = path.join(srcPath, dir)
  const srcFiles = await getFiles(location, (item) => item.path.endsWith('.js') && !item.path.endsWith('index.js'))
  const filesContents = await readFiles(srcFiles)
  const filesComments = srcFiles.map((location, index) => {
    const fnName = path.basename(location).replace(/\.js$/, '')
    const matter = getMatter(fnName, dir)
    const doc = matter.concat(extractComments(filesContents[index])).concat(getRuleImport(fnName))
    return { comments: doc.join('\n'), location }
  })
  await writeDocs(docsDir, filesComments)
}