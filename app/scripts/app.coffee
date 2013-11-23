'use strict'

angular.module('rcukApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute',
  'ngAnimate',
])
  .config ($routeProvider, $locationProvider) ->
    $routeProvider
      .when '/',
        templateUrl: 'views/main.html'
        controller: 'MainCtrl'
      .when '/result/:searchTerm',
        templateUrl: 'views/result.html'
        controller: 'ResultCtrl'
      .otherwise
        redirectTo: '/'