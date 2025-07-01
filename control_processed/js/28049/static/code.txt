function errorAndExit(msg, logMe) {
  // @todo Only trigger if `verbosity > 1`
  if (logMe) {
    // Adding some empty lines before error message for readability
    console.log();
    console.log();
    console.log(logMe);
  }
  error(`Error: ${msg}`);

  // There's a few ways to handle exiting

  // This is suggested and it's nice b/c it let's I/O finish up, but if an error happens on a watch task, it doesn't exit, b/c this will exit once the event loop is empty.
  // process.exitCode = 1;

  // This stops everything instantly and guarantees a killed program, but there's comments on the InterWebs about how it can be bad b/c I/O (like file writes) might not be done yet. I also have suspicions that this can lead to child processes never getting killed and running indefinitely - perhaps what leads to ports not being available
  // process.exit(1);

  // From docs for `process.nextTick` : "Once the current turn of the event loop turn runs to completion, all callbacks currently in the next tick queue will be called. This is not a simple alias to setTimeout(fn, 0). It is much more efficient. It runs before any additional I/O events (including timers) fire in subsequent ticks of the event loop."
  // This exits during watches correctly, and I *think* it'll let the I/O finish, but I'm not 100%
  process.nextTick(() => {
    process.exit(1);
  });
}