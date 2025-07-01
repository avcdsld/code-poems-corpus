function dummyP(n) {    
    return function lifted() {
        var deferred = Promise.pending();
        timers.setTimeout(nodeback, deferred, global.asyncTime || 100);
        return deferred.promise;
    }
}