function(event) {
      this.currentNb++;
      if (this.currentNb < this.length) pingAll(connList);
      //to avoid mysql2 taking all the server memory
      if (promiseMysql2 && promiseMysql2.clearParserCache)
        promiseMysql2.clearParserCache();
      if (mysql2 && mysql2.clearParserCache) mysql2.clearParserCache();
      console.log(event.target.toString());
      const drvType = event.target.options.drvType;
      const benchTitle =
        event.target.options.benchTitle +
        ' ( sql: ' +
        event.target.options.displaySql +
        ' )';
      const iteration = 1 / event.target.times.period;
      const variation = event.target.stats.rme;

      if (!bench.reportData[benchTitle]) {
        bench.reportData[benchTitle] = [];
      }
      if (drvType !== 'warmup') {
        bench.reportData[benchTitle].push({
          drvType: drvType,
          iteration: iteration,
          variation: variation
        });
      }
    }