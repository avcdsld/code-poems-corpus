function exec (cmd, userOptions) {
    if (cmd instanceof Array) {
      return cmd.map(function (cmd) { return exec(cmd, userOptions); });
    }
    try {
      const options = Object.create(defaultOptions);
      for (const key in userOptions) options[key] = userOptions[key];
      console.log(`\n--------\n ${cmd}`);
      return console.log(child_process.execSync(cmd, options).trim());
    } catch (err) {
      return err;
    }
  }