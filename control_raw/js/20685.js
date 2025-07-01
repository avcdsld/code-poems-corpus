function TimeHeap(options) {
    var self = this;
    options = options || {};

    self.timers = options.timers || globalTimers;
    self.minTimeout = options.minTimeout || null;
    self.array = [];
    self.expired = [];
    self.lastTime = self.timers.now();
    self.timer = null;
    self.end = 0;
    self.lastRun = 0;
    self.drainUntil = 0;

    self.scheduledDrain = null;

    self.boundDrainExpired = boundDrainExpired;

    function boundDrainExpired() {
        var now = self.scheduledDrain;
        self.scheduledDrain = null;

        self.drainExpired(now);
    }
}