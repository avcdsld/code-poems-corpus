function diffUpdateTriggers(props, oldProps) {
  if (oldProps === null) {
    return 'oldProps is null, initial diff';
  }

  // If the 'all' updateTrigger fires, ignore testing others
  if ('all' in props.updateTriggers) {
    const diffReason = diffUpdateTrigger(props, oldProps, 'all');
    if (diffReason) {
      return {all: true};
    }
  }

  const triggerChanged = {};
  let reason = false;
  // If the 'all' updateTrigger didn't fire, need to check all others
  for (const triggerName in props.updateTriggers) {
    if (triggerName !== 'all') {
      const diffReason = diffUpdateTrigger(props, oldProps, triggerName);
      if (diffReason) {
        triggerChanged[triggerName] = true;
        reason = triggerChanged;
      }
    }
  }

  return reason;
}