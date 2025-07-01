function completeJob(loader, job, callback) {
    var nextJob;

    loader.jobsInProgress--;

    if ((!loader.jobLimit || loader.jobsInProgress < loader.jobLimit) && loader.jobQueue.length > 0) {
        nextJob = loader.jobQueue.shift();
        nextJob.start();
        loader.jobsInProgress++;
    }

    callback(job.image, job.errorMsg, job.request);
}