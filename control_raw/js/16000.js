function initializeDatabase(silent, docCount) {
  var start, end, totalTime;
  var totalTimes = [];
  var totalMS = 0.0;

  if (typeof docCount === "undefined") {
    docCount = 5000;
  }

  arraySize = docCount;

  for (var idx = 0; idx < arraySize; idx++) {
    var v1 = genRandomVal();
    var v2 = genRandomVal();

    start = process.hrtime();
    samplecoll.insert({
      customId: idx,
      val: v1,
      val2: v2,
      val3: "more data 1234567890"
    });
    end = process.hrtime(start);
    totalTimes.push(end);
  }

  if (silent === true) {
    return;
  }

  for (var idx = 0; idx < totalTimes.length; idx++) {
    totalMS += totalTimes[idx][0] * 1e3 + totalTimes[idx][1] / 1e6;
  }

  // let's include final find which will probably punish lazy indexes more 
  start = process.hrtime();
  samplecoll.find({customIdx: 50});
  end = process.hrtime(start);
  totalTimes.push(end);

  //var totalMS = end[0] * 1e3 + end[1]/1e6;
  totalMS = totalMS.toFixed(2);
  var rate = arraySize * 1000 / totalMS;
  rate = rate.toFixed(2);
  console.log("load (individual inserts) : " + totalMS + "ms (" + rate + ") ops/s (" + arraySize + " documents)");
}