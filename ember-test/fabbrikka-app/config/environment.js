/* jshint node: true */

module.exports = function(environment) {
  var ENV = {
    modulePrefix: 'fabbrikka-app',
    environment: environment,
    rootURL: '/',
    locationType: 'auto',

    firebase:{
      apiKey: "AIzaSyAo0plv7MKPZrwn-g1Q1hwe9B2Gzx9REnM",
      authDomain: "fabbrikka-app.firebaseapp.com",
      databaseURL: "https://fabbrikka-app.firebaseio.com",
      storageBucket: "fabbrikka-app.appspot.com",
       messagingSenderId: "316429496146"
    },
    


    EmberENV: {
      FEATURES: {
        // Here you can enable experimental features on an ember canary build
        // e.g. 'with-controller': true
      },
      EXTEND_PROTOTYPES: {
        // Prevent Ember Data from overriding Date.parse.
        Date: false
      }
    },

    APP: {
      // Here you can pass flags/options to your application instance
      // when it is created
    }
  };

  if (environment === 'development') {
    // ENV.APP.LOG_RESOLVER = true;
    // ENV.APP.LOG_ACTIVE_GENERATION = true;
    // ENV.APP.LOG_TRANSITIONS = true;
    // ENV.APP.LOG_TRANSITIONS_INTERNAL = true;
    // ENV.APP.LOG_VIEW_LOOKUPS = true;
  }

  if (environment === 'test') {
    // Testem prefers this...
    ENV.locationType = 'none';

    // keep test console output quieter
    ENV.APP.LOG_ACTIVE_GENERATION = false;
    ENV.APP.LOG_VIEW_LOOKUPS = false;

    ENV.APP.rootElement = '#ember-testing';
  }

  if (environment === 'production') {

  }

  return ENV;
};
