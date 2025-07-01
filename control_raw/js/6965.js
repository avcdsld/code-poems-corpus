function getJobName(browserCap) {
  var browserName = getBrowserName(browserCap);

  return process.env.TRAVIS_PULL_REQUEST == 'false' ?
      'CO-' + process.env.TRAVIS_BRANCH + '-' + browserName :
      'PR-' + process.env.TRAVIS_PULL_REQUEST + '-' + browserName + '-' +
          process.env.TRAVIS_BRANCH;
}