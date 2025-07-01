async function compile(exitOnError = true) {
  config = config || (await asyncConfig());
  const startMessage = chalk.blue('Compiling Static Site...');
  const startTime = timer.start();
  let spinner;
  if (config.verbosity > 2) {
    console.log(startMessage);
  } else {
    spinner = ora(startMessage).start();
  }

  const pages = await getPages(config.srcDir);

  const renderPages = pages.map(async page => {
    const site = await getSiteData(pages);

    const layout = page.meta.layout ? page.meta.layout : 'default';
    const { ok, html, message } = await render(`@bolt/${layout}.twig`, {
      page,
      site,
    });

    if (!ok) {
      if (exitOnError) {
        log.errorAndExit(message);
      } else {
        log.error(message);
      }
    }

    const htmlFilePath = path.join(config.wwwDir, page.url);
    await mkdirp(path.dirname(htmlFilePath));
    await writeFile(htmlFilePath, html);
    if (config.verbosity > 3) {
      log.dim(`Wrote: ${htmlFilePath}`);
    }

    return true;
  });

  Promise.all(renderPages)
    .then(() => {
      const endMessage = chalk.green(
        `Compiled Static Site in ${timer.end(startTime)}`,
      );
      if (config.verbosity > 2) {
        console.log(endMessage);
      } else {
        spinner.succeed(endMessage);
      }
    })
    .catch(error => {
      console.log(error);
      const endMessage = chalk.red(
        `Compiling Static Site failed in ${timer.end(startTime)}`,
      );
      spinner.fail(endMessage);
    });
}