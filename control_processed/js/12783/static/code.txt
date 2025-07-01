function(props) {
  const { object, defaultRep } = props;
  const rep = getRep(object, defaultRep, props.noGrip);
  return rep(props);
}