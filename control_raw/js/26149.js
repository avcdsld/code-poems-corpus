function onApplicationStart(callback) {
    if (typeof Ember === 'undefined') {
      return;
    }

    const adapterInstance = requireModule('ember-debug/adapters/' + currentAdapter)['default'].create();

    adapterInstance.onMessageReceived(function(message) {
      if (message.type === 'app-picker-loaded') {
        sendApps(adapterInstance, getApplications());
      }

      if (message.type === 'app-selected') {
        const appInstance = getApplications().find(app => Ember.guidFor(app) === message.applicationId);

        if (appInstance && appInstance.__deprecatedInstance__) {
          bootEmberInspector(appInstance.__deprecatedInstance__);
        }
      }
    });

    var apps = getApplications();

    sendApps(adapterInstance, apps);

    var app;
    for (var i = 0, l = apps.length; i < l; i++) {
      app = apps[i];
      // We check for the existance of an application instance because
      // in Ember > 3 tests don't destroy the app when they're done but the app has no booted instances.
      if (app._readinessDeferrals === 0) {
        let instance = app.__deprecatedInstance__ || (app._applicationInstances && app._applicationInstances[0]);
        if (instance) {
          // App started
          setupInstanceInitializer(app, callback);
          callback(instance);
          break;
        }
      }
    }
    Ember.Application.initializer({
      name: 'ember-inspector-booted',
      initialize: function(app) {
        setupInstanceInitializer(app, callback);
      }
    });
  }