'use strict'

angular.module('rcukApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute',
  'ngAnimate',
  'ajoslin.promise-tracker',
])
  .config ["$routeProvider", "$locationProvider", ($routeProvider, $locationProvider) ->
    $routeProvider
      .when '/',
        templateUrl: 'views/main.html'
        controller: 'MainCtrl'
      .when '/result/:searchTerm',
        templateUrl: 'views/result.html'
        controller: 'ResultCtrl'
      .when '/person/:id',
        templateUrl: 'views/person.html'
        controller: 'PersonCtrl'
      .otherwise
        redirectTo: '/'
  ]
