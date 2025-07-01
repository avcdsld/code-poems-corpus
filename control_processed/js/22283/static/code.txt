function packRequirements() {
  if (this.options.zip) {
    if (this.serverless.service.package.individually) {
      return BbPromise.resolve(this.targetFuncs)
        .map(f => {
          if (!get(f, 'module')) {
            set(f, ['module'], '.');
          }
          return f;
        })
        .then(funcs => uniqBy(funcs, f => f.module))
        .map(f => {
          this.serverless.cli.log(
            `Zipping required Python packages for ${f.module}...`
          );
          f.package.include.push(`${f.module}/.requirements.zip`);
          return addTree(
            new JSZip(),
            `.serverless/${f.module}/requirements`
          ).then(zip => writeZip(zip, `${f.module}/.requirements.zip`));
        });
    } else {
      this.serverless.cli.log('Zipping required Python packages...');
      this.serverless.service.package.include.push('.requirements.zip');
      return addTree(new JSZip(), '.serverless/requirements').then(zip =>
        writeZip(zip, path.join(this.servicePath, '.requirements.zip'))
      );
    }
  }
}