async function getExtraTasks() {
  config = config || (await getConfig());

  switch (config.env) {
    case 'pl':
      extraTasks.patternLab = require('./pattern-lab-tasks');
      break;
    case 'static':
      extraTasks.static = require('./static-tasks');
      break;
    case 'pwa':
      delete require.cache[require.resolve('./api-tasks')];
      extraTasks.api = require('./api-tasks');
      extraTasks.patternLab = require('./pattern-lab-tasks');
      extraTasks.static = require('./static-tasks');
      break;
  }

  if (config.wwwDir) {
    extraTasks.server = require('./server-tasks');
  }

  return extraTasks;
}