async function execAndReport({ cmd, name }) {
  try {
    const {
      failed,
      // code,
      // timedOut,
      stdout,
      stderr,
      // message,
    } = await execa.shell(cmd);
    process.stdout.write(stdout);
    process.stderr.write(stderr);
    await setCheckRun({
      name,
      status: 'completed',
      conclusion: 'success',
      output: {
        title: name,
        summary: `Ran ${cmd}`,
      },
    });
    return failed;
  } catch (err) {
    const {
      failed,
      // code,
      // timedOut,
      stdout,
      stderr,
      message,
    } = err;
    process.stdout.write(stdout);
    process.stderr.write(stderr);
    await setCheckRun({
      name,
      status: 'completed',
      conclusion: 'failure',
      output: {
        title: name,
        summary: `Ran ${cmd}`,
        text: `
<pre><code>
${message}
</code></pre>
        `.trim(),
      },
    });

    return failed;
  }
}