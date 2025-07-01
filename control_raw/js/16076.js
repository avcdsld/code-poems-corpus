function WorkerHandler(script, _options) {
  this.script = script || getDefaultWorker();
  var options = _options || {};
  this.debugPort = options.debugPort;

  if (environment.platform == 'browser') {
    // check whether Worker is supported by the browser
    // Workaround for a bug in PhantomJS (Or QtWebkit): https://github.com/ariya/phantomjs/issues/14534
    if (typeof Worker !== 'function' && (typeof Worker !== 'object' || typeof Worker.prototype.constructor !== 'function')) {
      throw new Error('WorkerPool: Web workers not supported by the browser');
    }

    this.worker = setupBrowserWorker(this.script, Worker);
  } else {
    var WorkerThreads;

    if (options.nodeWorker === 'thread') {
      WorkerThreads = ensureWorkerThreads();
      this.worker = setupWorkerThreadWorker(this.script, WorkerThreads);
    } else if (options.nodeWorker === 'auto') {
      WorkerThreads = tryRequire('worker_threads');
      if (WorkerThreads) {
        this.worker = setupWorkerThreadWorker(this.script, WorkerThreads);
      } else {
        this.worker = setupProcessWorker(this.script, resolveForkOptions(options), require('child_process'));
      }
    } else {
      this.worker = setupProcessWorker(this.script, resolveForkOptions(options), require('child_process'));
    }
  }

  var me = this;

  // The ready message is only sent if the worker.add method is called (And the default script is not used)
  if (!script) {
    this.worker.ready = true;
  }

  // queue for requests that are received before the worker is ready
  this.requestQueue = [];
  this.worker.on('message', function (response) {
    if (typeof response === 'string' && response === 'ready') {
      me.worker.ready = true;
      dispatchQueuedRequests();
    } else {
      // find the task from the processing queue, and run the tasks callback
      var id = response.id;
      var task = me.processing[id];
      if (task !== undefined) {
        // remove the task from the queue
        delete me.processing[id];

        // test if we need to terminate
        if (me.terminating === true) {
          // complete worker termination if all tasks are finished
          me.terminate();
        }

        // resolve the task's promise
        if (response.error) {
          task.resolver.reject(objectToError(response.error));
        }
        else {
          task.resolver.resolve(response.result);
        }
      }
    }
  });

  // reject all running tasks on worker error
  function onError(error) {
    me.terminated = true;
    if (me.terminating && me.terminationHandler) {
      me.terminationHandler(me);
    }
    me.terminating = false;

    for (var id in me.processing) {
      if (me.processing[id] !== undefined) {
        me.processing[id].resolver.reject(error);
      }
    }
    me.processing = Object.create(null);
  }

  // send all queued requests to worker
  function dispatchQueuedRequests()
  {
    me.requestQueue.forEach(me.worker.send.bind(me.worker));
    me.requestQueue = [];
  }

  var worker = this.worker;
  // listen for worker messages error and exit
  this.worker.on('error', onError);
  this.worker.on('exit', function (exitCode, signalCode) {
    var message = 'Workerpool Worker terminated Unexpectedly\n';

    message += '    exitCode: `' + exitCode + '`\n';
    message += '    signalCode: `' + signalCode + '`\n';

    message += '    workerpool.script: `' +  me.script + '`\n';
    message += '    spawnArgs: `' +  worker.spawnargs + '`\n';
    message += '    spawnfile: `' + worker.spawnfile + '`\n'

    message += '    stdout: `' + worker.stdout + '`\n'
    message += '    stderr: `' + worker.stderr + '`\n'

    onError(new Error(message));
  });

  this.processing = Object.create(null); // queue with tasks currently in progress

  this.terminating = false;
  this.terminated = false;
  this.terminationHandler = null;
  this.lastId = 0;
}