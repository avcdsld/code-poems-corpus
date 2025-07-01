async function unlink(args: Array<string>, ctx: ConfigT) {
  const packageName = args[0];

  const {[packageName]: dependency, ...otherDependencies} = ctx.dependencies;

  if (!dependency) {
    throw new CLIError(`
      Failed to unlink "${packageName}". It appears that the project is not linked yet.
    `);
  }

  const dependencies = values(otherDependencies);
  try {
    if (dependency.hooks.preulink) {
      await dependency.hooks.preulink();
    }
    unlinkDependency(
      ctx.platforms,
      ctx.project,
      dependency,
      packageName,
      dependencies,
    );
    if (dependency.hooks.postunlink) {
      await dependency.hooks.postunlink();
    }
  } catch (error) {
    throw new CLIError(
      `Something went wrong while unlinking. Reason ${error.message}`,
      error,
    );
  }

  // @todo move all these to above try/catch
  // @todo it is possible we could be unlinking some project assets in case of duplicate
  const assets = difference(
    dependency.assets,
    flatMap(dependencies, d => d.assets),
  );

  if (assets.length === 0) {
    return;
  }

  Object.keys(ctx.platforms || {}).forEach(platform => {
    const projectConfig = ctx.project[platform];
    const linkConfig =
      ctx.platforms[platform] &&
      ctx.platforms[platform].linkConfig &&
      ctx.platforms[platform].linkConfig();
    if (!linkConfig || !linkConfig.unlinkAssets || !projectConfig) {
      return;
    }

    logger.info(`Unlinking assets from ${platform} project`);
    // $FlowFixMe
    linkConfig.unlinkAssets(assets, projectConfig);
  });

  logger.info(
    `${packageName} assets has been successfully unlinked from your project`,
  );
}