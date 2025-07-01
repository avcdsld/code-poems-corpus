function PageTitle(props) {
  const { activePage } = React.useContext(PageContext);

  if (!activePage) {
    throw new Error('Missing activePage.');
  }

  const title = pageToTitleI18n(activePage, props.t);

  return props.children(title);
}