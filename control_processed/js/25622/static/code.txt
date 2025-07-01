async function defaultSection(ctx, next) {
  const sections = await _getContentSections();
  ctx.state.section = sections[0] || await Section.findGeneral();
  await next();
}