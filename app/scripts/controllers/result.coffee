'use strict'

angular.module('rcukApp')
  .controller 'ResultCtrl', ["$scope", "Search", "$routeParams", "$location", ($scope, Search, $routeParams, $location) ->
    Search.query $routeParams.searchTerm, $scope

    $scope.showPerson = (id) ->
      console.log(id)
      $location.path("/person/"+ id)
  ]
